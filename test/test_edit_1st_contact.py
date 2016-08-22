# -*- coding: utf-8 -*-
from model.contact import Contact

# Вынесем отдельный объект
new_contact = Contact(firstname="Jonny", middlename="W", lastname="Exesium", nickname="Happy", title="Engineer",
                      company="ATOL", address="Moscow", mobile="+7 985 966 44 24", work="+7 (495) 730-74-20",
                      email="i.petrov@gmail.com", b_day=26, b_month=9, b_year="1982")


def test_edit_1st(app):
    app.contact.edit_1st(new_contact)
