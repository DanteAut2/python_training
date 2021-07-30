from model.group import Group
from model.contact import Contact
import random

def test_delete_contact_from_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_groups_with_contacts()) == 0:
        groups = db.get_group_list()
        group = random.choice(groups)
        contacts = db.get_contacts_not_in_group()
        contact = random.choice(contacts)
        app.contact.add_contact_in_group(contact.id, group.id)
    groups = db.get_groups_with_contacts()
    group = random.choice(groups)
    old_contacts = db.get_contacts_in_group()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_from_group(contact.id, group.id)
    new_contacts = db.get_contacts_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)