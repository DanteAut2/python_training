from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="sdfdsfg", first_mail="sdfgsdffg", second_address="fgdsfgsdfg"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="sdfdsfg", first_mail="sdfgsdffg", second_address="fgdsfgsdfg")
    app.contact.modify_first_contact(contact)
    contact.id = old_contacts[0].id
    contact.last_name = old_contacts[0].last_name
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)