import re
from model.contact import Contact


def test_all_contact_data_on_home_page(app, db):
    check_empty_filling_db(app, db)
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)

def clean(s):
    return re.sub("[() -]", "", s)


def check_empty_filling_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="figu", lastname="ihfuge", mobile="74575", homephone="65476", workphone="576", secondaryphone="33",
                      address='jediafhc', email='odfej', email2='frdj', email3='jdfr'))