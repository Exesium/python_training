# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

# Вынесем отдельный объект
new_contact = Contact(firstname="Ivan", lastname="Petrov", nickname="Happy", title="Engineer",
                             company="ATOL", address="Moscow", mobile="+7 985 966 44 24",
                             work="+7 (495) 730-74-20", email="i.petrov@gmail.com")


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contact(new_contact)
    app.session.logout()
