from model.group import Group
import random


def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    group_edited = Group(gr_name="Name changed")
    app.group.edit_group_by_id(group.id, group_edited)
    new_groups = db.get_group_list()
    old_groups[index] = group_edited
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, gr_name=group.gr_name.strip())
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)