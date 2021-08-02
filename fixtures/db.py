
import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), gr_name=name, gr_header=header, gr_footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile," +
                           "work, fax, email, email2, email3, bday, bmonth, byear, aday, amonth, ayear," +
                           "address2, phone2, notes from addressbook where deprecated='0000-00-00 00:00:00' ")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile,
                 work, fax, email, email2, email3, bday, bmonth, byear, aday, amonth, ayear,
                 address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                 title=title, company=company, street=address, homephone=home, mobilephone=mobile, workphone=work, fax=fax,
                 email=email, email2=email2, email3=email3, birthday_day=bday, birthday_month=bmonth, birthday_year=byear,
                anniversary_day=aday, anniversary_month=amonth, anniversary_year=ayear, address2=address2, phone2=phone2, note=notes))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()