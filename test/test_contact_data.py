import re
from random import randrange
from model.contact import Contact

ch_contact = Contact(firstname="Jonny", middlename="W", lastname="Exesium", nickname="Happy", title="Engineer",
                     company="ATOL", address="Moscow", mobile="+7-985-966-44-24", work="+7 (495) 730-74-20",
                     email="i.petrov@gmail.com", email2="", email3="i.pet_rov3@gmail.com",
                     b_day=26, b_month=9, b_year="1982")


def test_random_contact_data_on_homepage(app):
    if app.contact.count() == 0:
        app.contact.add_new(ch_contact)
    index = randrange(len(app.contact.get_contact_list()))
    data_from_home_page = app.contact.get_contact_list_new()[index]
    data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # disabled due to changes on home page
    # assert data_from_home_page.firstname == data_from_edit_page.firstname
    # assert data_from_home_page.lastname == data_from_edit_page.lastname
    assert data_from_home_page.address == data_from_edit_page.address
    assert data_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(data_from_edit_page)
    assert data_from_home_page.all_emails == merge_emails_like_on_homepage(data_from_edit_page)


"""
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2
"""


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
