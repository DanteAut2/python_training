import re
from model.contact import Contact


def test_all_contact_data_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_db)
    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i].id == contact_from_db[i].id
        assert contact_from_home_page[i].firstname == contact_from_db[i].firstname
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[i])


def clean(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact_helper):
     return "\n".join(filter(lambda x: x!= "", map(lambda x: clean(x),
                                                  filter(lambda x: x is not None, [contact_helper.email,
                                                                                contact_helper.email2,
                                                                                contact_helper.email3]))))


def merge_phones_like_on_home_page(contact_helper):
    return "\n".join(filter(lambda x: x!= "", map(lambda x: clean(x),
                                                  filter(lambda x: x is not None, (contact_helper.homephone,
                                                         contact_helper.mobilephone, contact_helper.workphone,
                                                                                   contact_helper.secondaryphone)))))