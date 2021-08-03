
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    old_contacts = db.get_contacts_list()
    app.contact.checker_that_old_contacts_not_zero(old_contacts)
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    contact_to_edit = Contact(firstname="Test edit", middlename="Midtest edit", lastname="Lasttest edit", nickname="Nickname test edit", title="Mrs edit", company="Test Company edit", street="5th Avenue edit",
                      homephone="15 edit", mobilephone="111999333444", workphone="12123342444", fax="2345645444", email="testedit@test.com", birthday_day="1",
                      birthday_month="August", birthday_year="1990", anniversary_day="1",
                      anniversary_month="October", anniversary_year="1990", address2="Sec address edit", phone2="163434444", note="testtesttest note edit")
    app.contact.edit_contact_by_id(contact.id, contact_to_edit)
    new_contacts = db.get_contacts_list()
    old_contacts[index] = contact_to_edit
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        new_contacts = map(clean, db.get_contacts_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)