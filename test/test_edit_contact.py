# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# Вынесем отдельный объект
ch_contact = Contact(firstname="Jonny", middlename="W", lastname="Exesium", nickname="Happy", title="Engineer",
                     company="ATOL", address="Moscow", mobile="+7-985-966-44-24", work="+7 (495) 730-74-20",
                     email="i.petrov@gmail.com", email2="", email3="i.pet_rov3@gmail.com",
                     b_day=26, b_month=9, b_year="1982")
empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(empty_contact)
    old_cs = db.get_contact_list()
    con_for_edit = random.choice(old_cs)
    ch_contact.identity = con_for_edit.identity
    old_cs.remove(con_for_edit)
    app.contact.edit_by_id(ch_contact.identity, ch_contact)
    old_cs.append(ch_contact)
    new_cs = db.get_contact_list()
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_cs, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
