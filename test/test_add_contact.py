# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="sdfdsfg", home_number="fdsfgsdfg", first_mail="sdfgsdffg",
            second_address="fgdsfgsdfg", last_name="dsgdsfg")
    contact.id = old_contacts[0].id
    contact.last_name = old_contacts[0].last_name
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)