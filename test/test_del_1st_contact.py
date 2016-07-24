# -*- coding: utf-8 -*-


def test_del_1st_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_1st()
    app.session.logout()
