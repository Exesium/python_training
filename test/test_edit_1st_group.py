# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_1st_group(app):
    app.group.edit_1st(Group(name="CHANGED_GROUP!"))
