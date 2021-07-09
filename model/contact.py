from sys import maxsize


class Contact:


    def __init__(self, id=None, lastname=None, firstname=None, homephone=None, first_mail=None, second_address=None, workphone=None, mobilephone=None, secondaryphone=None):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.first_mail = first_mail
        self.second_address = second_address


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize