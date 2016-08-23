# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_group_name_by_index(app):
    group = Group(name="CHANGED_GROUP!")
    if app.group.count() == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.edit_by_index(index, group)
    group.id = old_groups[index].id
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""
def test_edit_1st_group_header(app):
    group = Group(header="CHANGED_HEADER!")
    if app.group.count() == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    old_groups = app.group.get_group_list()
    app.group.edit_1st(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""
