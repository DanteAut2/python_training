
from model.group import Group
from model.contact import Contact

def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, gr_name=group.gr_name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contacts_list(app, db):
    ui_list = app.contact.get_contacts_list()

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = map(clean, db.get_contacts_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)