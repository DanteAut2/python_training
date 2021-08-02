
import re
from model.contact import Contact


def test_phones_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contacts_list()
    sorted_contacts_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(), homephone=contact.homephone.strip(), mobilephone=contact.mobilephone.strip(),
                       workphone=contact.workphone.strip(), phone2=contact.phone2.strip(), email=contact.email.strip(), email2=contact.email2.strip(), email3=contact.email3.strip(), street=contact.street.strip())

    contact_from_database = list(map(clean, db.get_contacts_list()))
    sorted_contacts_from_database = sorted(contact_from_database, key=Contact.id_or_max)

    assert sorted_contacts_from_home_page == sorted_contacts_from_database  # compare firstname and lastname

    phones_from_database = list(map(merge_phones_like_on_home_page, sorted_contacts_from_database))
    for (c, p) in zip(sorted_contacts_from_home_page, phones_from_database):
        assert c.all_phones_from_home_page == p

    emails_from_database = list(map(merge_emails_like_on_home_page, sorted_contacts_from_database))
    for (c, e) in zip(sorted_contacts_from_home_page, emails_from_database):
        assert c.all_emails_from_home_page == e

    for (c, s) in zip(sorted_contacts_from_home_page, sorted_contacts_from_database):
        assert c.street == s.street



def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))



def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))