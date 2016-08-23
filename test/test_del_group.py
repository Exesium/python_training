# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.del_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)