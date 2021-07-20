import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Contact(lastname="", firstname="", homephone="", first_mail="",
                      second_address="")] + [
    Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 20),
            homephone=random_string("homephone", 20), first_mail=random_string("first_mail", 20),
            second_address=random_string("second_address", 20))
    for last_name in range(2)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))