from model.group import Group
import random

def test_modify_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="sdfgdsfg", footer="gdfhgdfghd")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)