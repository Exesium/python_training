# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    new_contact = json_contacts
    old_cs = app.contact.get_contact_list()
    app.contact.add_new(new_contact)
    assert len(old_cs) + 1 == app.contact.count()
    new_cs = app.contact.get_contact_list()
    old_cs.append(new_contact)
    assert sorted(old_cs, key=Contact.id_or_max) == sorted(new_cs, key=Contact.id_or_max)
