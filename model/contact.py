from sys import maxsize


class Contact:


    def __init__(self, id=None, lastname=None, firstname=None, homephone=None, first_mail=None,
                 second_address=None, workphone=None, mobilephone=None, secondaryphone=None,
                 email=None, email2=None, email3=None, address=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, phone2=None):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.first_mail = first_mail
        self.second_address = second_address
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize