# -*- coding: utf-8 -*-
from model.group import Group


def test_del_1st_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    app.group.del_1st()
