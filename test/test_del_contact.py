# -*- coding: utf-8 -*-
from model.contact import Contact
import random
empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(empty_contact)
    old_cs = db.get_contact_list()
    con = random.choice(old_cs)
    app.contact.del_by_id(con.identity)
    new_cs = db.get_contact_list()
    old_cs.remove(con)
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_cs, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
