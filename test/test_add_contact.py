# -*- coding: utf-8 -*-
from model.contact import Contact

# Вынесем отдельный объект
new_contact = Contact(firstname="Jon", lastname="Exesium", nickname="Happy", title="Engineer",
                             company="ATOL", address="Moscow", mobile="+7 985 966 44 24",
                             work="+7 (495) 730-74-20", email="i.petrov@gmail.com")


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(new_contact)
    app.session.logout()
