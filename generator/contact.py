from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbol = string.digits + string.ascii_letters
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_digits(prefix, maxlen):
    symbol = string.digits
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")] + [
            Contact(firstname=random_string('FN',10), middlename=random_string('MN',10), lastname=random_string('LN',10),
                    nickname=random_string('Nick',10), title=random_string('Title',10), company=random_string('Co',10),
                    address=random_string('Moscow',10), home=random_digits('+',12), work=random_digits('+',12),
                    mobile=random_digits('+',12), fax=random_digits('+',12), email=random_string('Email',10),
                    email2=random_string('Email',10), email3=random_string('Email',10), b_day=random_digits('',1),
                    b_month=random_digits('',1), b_year=random_digits('',4),
                    phone2=random_digits('+',12)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
