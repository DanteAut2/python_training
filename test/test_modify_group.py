from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.chose_first_group()
    app.group.click_edit_group()
    app.group.modify(Group(name="sdfgdsfg", header="gsdfgsdgf", footer="gdfhgdfghd"))
    app.session.logout()