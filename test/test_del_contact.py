from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="sdfdsfg", first_mail="sdfgsdffg",
                                           second_address="fgdsfgsdfg"))
    app.contact.delete_first_contact()