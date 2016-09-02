# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact


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
                    phone2=random_digits('+',12)) for i in range(5)]


@pytest.mark.parametrize('new_contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, new_contact):
    old_cs = app.contact.get_contact_list()
    app.contact.add_new(new_contact)
    assert len(old_cs) + 1 == app.contact.count()
    new_cs = app.contact.get_contact_list()
    old_cs.append(new_contact)
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
