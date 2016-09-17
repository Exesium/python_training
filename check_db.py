from fixture.db import DbFixture


# conn = mysql.connector.connect(host='127.0.0.1', database='addressbook', user='root', password='')

abc = DbFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    currrr = abc.get_contact_list()
    for row in currrr:
        print(row)
    print(len(currrr))
    print("----------------------------------------------------")

finally:
    abc.destroy()
