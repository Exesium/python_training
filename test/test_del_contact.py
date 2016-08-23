# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_del_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(empty_contact)
    old_cs = app.contact.get_contact_list()
    index = randrange(len(old_cs))
    app.contact.del_by_index(index)
    assert len(old_cs) - 1 == app.contact.count()
    new_cs = app.contact.get_contact_list()
    old_cs[index:index+1] = []
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
