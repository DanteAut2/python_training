from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="sdfdsfg", first_mail="sdfgsdffg", second_address="fgdsfgsdfg"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="sdfdsfg", first_mail="sdfgsdffg", second_address="fgdsfgsdfg")
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)