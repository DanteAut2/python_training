from sys import maxsize


class Group:
    def __init__(self, gr_name=None, gr_header=None, gr_footer=None, id=None):
        self.gr_name = gr_name
        self.gr_header = gr_header
        self.gr_footer = gr_footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.gr_name, self.gr_header, self.gr_footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.gr_name == other.gr_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize