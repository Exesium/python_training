# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_group_name_by_id(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    old_groups = db.get_group_list()
    group_for_edit = random.choice(old_groups)
    group.identity = group_for_edit.identity
    old_groups.remove(group_for_edit)
    app.group.edit_by_id(group.identity, group)
    old_groups.append(group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
