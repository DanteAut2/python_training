# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="sdfdsfg", home_number="fdsfgsdfg", first_mail="sdfgsdffg",
                               second_address="fgdsfgsdfg"))