# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, fax=None, b_day=None, b_month=None, b_year=None, identity=None,
                 home=None, mobile=None, work=None, phone2=None, all_phones_from_homepage=None,
                 email=None, email2=None, email3=None, all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.identity = identity
        self.phone2 = phone2
        self.all_emails = all_emails
        self.all_phones_from_homepage = all_phones_from_homepage

    def __repr__(self):
        return "%s:%s %s" % (self.identity, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.identity is None or other.identity is None or self.identity == other.identity) \
               and self.firstname == other.firstname\
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.identity:
            return int(self.identity)
        else:
            return maxsize
