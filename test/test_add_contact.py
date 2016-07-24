# -*- coding: utf-8 -*-
from model.contact import Contact

# Вынесем отдельный объект
new_contact = Contact(firstname="Jon", middlename="S", lastname="Exesium", nickname="Happy", title="Engineer",
                      company="ATOL", address="Moscow", mobile="+7 985 966 44 24", work="+7 (495) 730-74-20",
                      email="i.petrov@gmail.com", b_day=3, b_month=2, b_year="1970")
empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(new_contact)
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(empty_contact)
    app.session.logout()
