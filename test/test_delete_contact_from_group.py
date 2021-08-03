import random

def test_delete_contact_from_group(app, dbORM):
    dbORM.checker_that_we_have_groups_with_contacts(app)
    groups_with_contacts = dbORM.get_groups_with_contacts()
    group = random.choice(groups_with_contacts)
    contacts_in_group = dbORM.get_contacts_in_groups(group)
    contact = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact.id, group)
    new_contacts_with_groups = dbORM.get_contacts_in_groups(group)
    contacts_in_group.remove(contact)
    assert contacts_in_group == new_contacts_with_groups