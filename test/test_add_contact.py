# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    new_contact = json_contacts
    old_cs = db.get_contact_list()
    app.contact.add_new(new_contact)
    new_cs = db.get_contact_list()
    old_cs.append(new_contact)
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_cs, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
