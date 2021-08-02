from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.add_new_contact(Contact(firstname="Testik", middlename="Midtest", lastname="Lasttest", nickname="Nickname test", title="Mrs", company="Test Company", street="5th Avenue",
                                            homephone="15", mobilephone="111999333", workphone="12123342", fax="2345645", email="test@test.com", birthday_day="11",
                                            birthday_month="July", birthday_year="1991", anniversary_day="8", anniversary_month="November", anniversary_year="1991", address2="Sec address", phone2="163434", note="testtesttest note"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        new_contacts = map(clean, db.get_contacts_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)