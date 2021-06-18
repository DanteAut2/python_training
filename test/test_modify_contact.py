from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.chose_first_contact()
    app.contact.modify(Contact(first_name="sdfdsfg", home_number="fdsfgsdfg", first_mail="sdfgsdffg",
                               second_address="fgdsfgsdfg"))
    app.session.logout()