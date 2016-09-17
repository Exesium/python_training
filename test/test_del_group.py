# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="When_there_is_no_GROUP"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.del_by_id(group.identity)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
