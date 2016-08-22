# -*- coding: utf-8 -*-
from model.contact import Contact
empty_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        mobile="", work="", email="", b_day=0, b_month=0, b_year="")


def test_del_1st_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(empty_contact)
    app.contact.del_1st()
