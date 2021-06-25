from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="sdfdsfg", first_mail="sdfgsdffg",
                                           second_address="fgdsfgsdfg"))
    app.contact.chose_first_contact()
    app.contact.modify_first_contact(Contact(first_name="sdfdsfg", first_mail="sdfgsdffg",
                                           second_address="fgdsfgsdfg"))