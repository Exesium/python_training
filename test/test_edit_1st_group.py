# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_1st_group((Group(name="CHANGED_GROUP!", header="xxxyyyzzz", footer="Edit group OK")))
    app.session.logout()
