
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, dbORM):
    old_contacts = dbORM.get_contact_list()
    old_groups = dbORM.get_group_list()
    if len(old_contacts) == 0:
        app.contact.add_new_contact(Contact(firstname="Testik", middlename="Midtest", lastname="Lasttest", nickname="Nickname test",
                                            title="Mrs", company="Test Company", street="5th Avenue", homephone="15", mobilephone="111999333", workphone="12123342", fax="2345645", email="test@test.com",
                                            birthday_day="11", birthday_month="July", birthday_year="1991", anniversary_day="8", anniversary_month="November", anniversary_year="1991", address2="Sec address", phone2="163434",
                                            note="testtesttest note"))
    if len(old_groups) == 0:
        app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    available_groups = []
    for i in old_groups:
        number_of_contacts_in_group = len(dbORM.get_contacts_in_groups(i))
        if number_of_contacts_in_group != len(old_contacts):
            available_groups.append(i)
    if len(available_groups) == 0:
        new_available_group = app.group.create(Group(gr_name="Test group new", gr_header="test header", gr_footer="test footer"))
        available_groups.append(new_available_group)
    group = random.choice(available_groups)
    contacts_not_in_group = dbORM.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact.id, group)