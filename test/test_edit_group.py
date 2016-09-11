# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_group_name_by_index(app, json_groups):
    group = json_groups
    if app.group.count() == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.edit_by_index(index, group)
    group.identity = old_groups[index].identity
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
