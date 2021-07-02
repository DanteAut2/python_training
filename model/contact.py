from sys import maxsize


class Contact:


    def __init__(self, first_name=None, home_number=None, first_mail=None, second_address=None, id=None, last_name=None):
        self.first_name = first_name
        self.home_number = home_number
        self.first_mail = first_mail
        self.second_address = second_address
        self.id = id
        self.last_name = last_name


    def __repr__(self):
        return "%s:%s" & (self.id, self.name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize