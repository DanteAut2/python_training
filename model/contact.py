from sys import maxsize


class Contact:


    def __init__(self, id=None, last_name=None, first_name=None, home_number=None, first_mail=None, second_address=None):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.home_number = home_number
        self.first_mail = first_mail
        self.second_address = second_address


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name and self.first_name == other.first_name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize