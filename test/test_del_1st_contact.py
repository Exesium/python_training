# -*- coding: utf-8 -*-
from model.contact import Contact
empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_del_1st_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(empty_contact)
    old_cs = app.contact.get_contact_list()
    app.contact.del_1st()
    new_cs = app.contact.get_contact_list()
    assert len(old_cs) - 1 == len(new_cs)
    old_cs[0:1] = []
    assert len(old_cs) == len(new_cs)
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
