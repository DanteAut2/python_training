from model.contact import Contact


def test_add_contact(app):
    app.contact.chose_first_contact()
    app.contact.modify_first_contact(Contact(first_name="sdfdsfg", first_mail="sdfgsdffg",
                                           second_address="fgdsfgsdfg"))