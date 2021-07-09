import re


def test_data_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clean(s):
    return re.sub('\s+', ' ', s.strip())


def merge_emails_like_on_home_page(contact_helper):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clean(x),
                                                   filter(lambda x: x is not None, [contact_helper.email,
                                                                                    contact_helper.email2,
                                                                                    contact_helper.email3]))))
