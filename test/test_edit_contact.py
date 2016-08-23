# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

# Вынесем отдельный объект
ch_contact = Contact(firstname="Jonny", middlename="W", lastname="Exesium", nickname="Happy", title="Engineer",
                     company="ATOL", address="Moscow", mobile="+7 985 966 44 24", work="+7 (495) 730-74-20",
                     email="i.petrov@gmail.com", b_day=26, b_month=9, b_year="1982")
empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(empty_contact)
    old_cs = app.contact.get_contact_list()
    index = randrange(len(old_cs))
    app.contact.edit_by_index(index, ch_contact)
    ch_contact.id = old_cs[index].id
    assert len(old_cs) == app.contact.count()
    new_cs = app.contact.get_contact_list()
    old_cs[index] = ch_contact
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
