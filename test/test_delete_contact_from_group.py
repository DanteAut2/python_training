import random
from test.test_add_contact_in_group import test_add_contact_in_group


def test_delete_contact_from_group(app, dbORM):
    if len(dbORM.get_groups_with_contacts()) == 0:
        test_add_contact_in_group(app, dbORM)
    groups_with_contacts = dbORM.get_groups_with_contacts()
    group = random.choice(groups_with_contacts)
    contacts_in_group = dbORM.get_contacts_in_groups(group)
    contact = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact.id, group)