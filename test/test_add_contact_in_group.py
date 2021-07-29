from model.contact import Contact
from model.group import Group
import random
from fixtures.orm import ORMFixture


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def check_empty_filling(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))


def test_add_contact_to_group(app, db):
    check_empty_filling(app, db)
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    random_group_number = random.randint(1, len(groups))
    random_group_id = groups[random_group_number-1].id
    contacts_before_add = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))
    app.contact.add_contact_to_group_by_id(contact.id, random_group_number)
    contacts_after_add = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))
    assert contacts_before_add + 1 == contacts_after_add


def test_delete_contact_from_group(app, db):
    global orm
    check_empty_filling(app, db)
    groups = db.get_group_list()
    random_group_number = random.randint(1, len(groups))
    random_group_id = groups[random_group_number - 1].id
    contacts_before_delete = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))
    if contacts_before_delete == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group_by_id(contact.id, random_group_number=random_group_number)
        app.contact.delete_contact_from_group_by_id(group_id=random_group_id, orm=orm)
        contacts_after_delete = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))
        assert contacts_before_delete - 1 == contacts_after_delete