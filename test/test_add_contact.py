# -*- coding: utf-8 -*-
from model.contact import Contact


empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_add_contact(app):
    new_contact = Contact(firstname="Jon", middlename="S", lastname="Exesium", nickname="Happy", title="Engineer",
                          company="ATOL", address="Moscow", mobile="+7 985 966 44 24", work="+7 (495) 730-74-20",
                          email="i.petrov@gmail.com", b_day=3, b_month=2, b_year="1970")
    old_cs = app.contact.get_contact_list()
    app.contact.add_new(new_contact)
    new_cs = app.contact.get_contact_list()
    assert len(old_cs) + 1 == len(new_cs)
    old_cs.append(new_contact)
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    app.contact.add_new(empty_contact)
