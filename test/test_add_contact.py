# -*- coding: utf-8 -*-
from model.contact import Contact


empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_add_contact(app):
    new_contact = Contact(firstname="Jon", middlename="S", lastname="Exesium", nickname="Happy", title="Engineer",
                          company="ATOL", address="Moscow", home="+7 (495) 012-34-34", work="+7 (495) 730-74-20",
                          mobile="+7-985-966-44-24", fax="+7 (495) 730-74-22", email="i.petrov@gmail.com",
                          email2="i.petrov_12@gmail.com", email3="i.pet_rov3@gmail.com",
                          b_day=3, b_month=2, b_year="1970", phone2="")
    old_cs = app.contact.get_contact_list()
    app.contact.add_new(new_contact)
    assert len(old_cs) + 1 == app.contact.count()
    new_cs = app.contact.get_contact_list()
    old_cs.append(new_contact)
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#    app.contact.add_new(empty_contact)
