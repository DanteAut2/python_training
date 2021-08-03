from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_phones(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_emails(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("fname", 10),  middlename=random_string("mname", 10), lastname=random_string("lname", 10),
          nickname=random_string("nick", 10), title=random_string("t", 5), company=random_string("comp", 10),
          street=random_string("address", 10), homephone=random_string_phones(10), mobilephone=random_string_phones(10),
          workphone=random_string_phones(10), fax=random_string_phones(10), email=random_string_emails(10)+"@test.com",
          birthday_day="11", birthday_month="July", birthday_year="1991", anniversary_day="8",
          anniversary_month="November", anniversary_year="1991", address2=random_string("addr2", 10), phone2=random_string_phones(10),
          note=random_string("note", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
        jsonpickle.set_encoder_options("json", indent=2)
        out.write(jsonpickle.encode(testdata))