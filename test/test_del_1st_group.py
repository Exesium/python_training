# -*- coding: utf-8 -*-


def test_del_1st_group(app):
    app.session.login(username="admin", password="secret")
    app.group.del_1st()
    app.session.logout()
