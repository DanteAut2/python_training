# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Contact(lastname="", firstname="", homephone="", first_mail="",
                      second_address="")] + [
    Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 20),
            homephone=random_string("homephone", 20), first_mail=random_string("first_mail", 20),
            second_address=random_string("second_address", 20))
    for last_name in range(2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)