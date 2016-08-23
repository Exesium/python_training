# -*- coding: utf-8 -*-
from model.group import Group


def test_del_1st_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    old_groups = app.group.get_group_list()
    app.group.del_1st()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
