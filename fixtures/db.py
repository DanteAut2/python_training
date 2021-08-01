import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password,
                                                  autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, email, address ,home, mobile, work, email2, email3,"
                           " phone2 from addressbook where deprecated='0000-00-00 00:00:00'")


            for row in cursor:
                (id, firstname, lastname, email, address, homephone, mobilephone, workphone, email2, email3,
                 phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, email=email, address=address,
                                    homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                                    email2=email2, email3=email3, phone2=phone2))
        finally:
            cursor.close()
        return list

    def get_groups_with_contacts(self):
        list = []

        with self.connection.cursor() as cursor:
            cursor.execute(
                "select distinct(group_id), 'dummy' from address_in_groups where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (group_id, dummy) = row
                list.append(Group(id=str(group_id)))
        return list


    def get_contacts_not_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select a.id, a.firstname, a.lastname, a.address, a.home, a.mobile, a.work, a.email, a.email2, a.email3, a.phone2 from addressbook a left join address_in_groups ag on ag.id=a.id where ag.id is null")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3, secondaryphone=phone2))
        finally:
            cursor.close()
        return list


    def get_contacts_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select distinct (a.id), a.firstname, a.lastname, a.address, a.home, a.mobile, a.work, a.email, a.email2, a.email3, a.phone2 from addressbook a inner join address_in_groups ag on ag.id=a.id")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3,
                                    secondaryphone=phone2))
        finally:
            cursor.close()
        return list


