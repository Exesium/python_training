# -*- coding: utf-8 -*-
from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, identity=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.identity = identity

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.identity, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.identity is None or other.identity is None or self.identity == other.identity) and self.name == other.name

    def id_or_max(self):
        if self.identity:
            return int(self.identity)
        else:
            return maxsize
