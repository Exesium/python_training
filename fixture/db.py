import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.conn = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.conn.autocommit = True

    def get_group_list(self):
        my_group_list = []
        cursor = self.conn.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                my_group_list.append(Group(identity=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return my_group_list

    def get_contact_list(self):
        my_con_list = []
        cursor = self.conn.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                my_con_list.append(Contact(identity=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return my_con_list

    def destroy(self):
        self.conn.close()
