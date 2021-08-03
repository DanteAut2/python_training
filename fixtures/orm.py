from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
import random
from fixtures import contact

class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        gr_name = Optional(str, column='group_name')
        gr_header = Optional(str, column='group_header')
        gr_footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        title = Optional(str, column='title')
        street = Optional(str, column='address')
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        fax = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        birthday_day = Optional(int, column='bday')
        birthday_month = Optional(str, column='bmonth')
        birthday_year = Optional(str, column='byear')
        anniversary_day = Optional(int, column='aday')
        anniversary_month = Optional(str, column='amonth')
        anniversary_year = Optional(str, column='ayear')
        address2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        note = Optional(str, column='notes')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)


    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), gr_name=group.gr_name, gr_header=group.gr_header, gr_footer=group.gr_footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, middlename=contact.middlename, lastname=contact.lastname,
                           nickname=contact.nickname, company=contact.company, title=contact.title, street=contact.street,
                           homephone=contact.homephone, mobilephone=contact.mobilephone, workphone=contact.workphone,
                           fax=contact.fax, email=contact.email, email2=contact.email2, email3=contact.email3,
                           birthday_day=contact.birthday_day, birthday_month=contact.birthday_month, birthday_year=contact.birthday_year,
                           anniversary_day=contact.anniversary_day, anniversary_month=contact.anniversary_month, anniversary_year=contact.anniversary_year,
                           address2=contact.address2, phone2=contact.phone2, note=contact.note)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_groups(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_groups_with_contacts(self):
        groups_with_contacts = []
        group_id = self.db.select("group_id FROM address_in_groups")
        for i in group_id:
            groups_with_contacts.append(Group(id=str(i)))
        return groups_with_contacts

    @db_session
    def checker_that_we_have_groups_with_contacts(self, app):
        if len(self.get_groups_with_contacts()) == 0:
            old_contacts = self.get_contact_list()
            old_groups = self.get_group_list()
            app.contact.checker_that_old_contacts_not_zero(old_contacts)
            app.group.checker_that_old_groups_not_zero(old_groups)
            available_groups = app.group.get_available_groups(old_groups, old_contacts, self)
            group = random.choice(available_groups)
            contacts_not_in_group = self.get_contacts_not_in_group(group)
            contact = random.choice(contacts_not_in_group)
            app.contact.add_contact_to_group(contact.id, group)