import mysql.connector
import pymysql.cursors

# conn = mysql.connector.connect(host='127.0.0.1', database='addressbook', user='root', password='')
con2 = pymysql.connect(host='127.0.0.1', database='addressbook', user='root', password='')


try:
    a = con2.get_server_info()
    cur = con2.cursor()
    cur.execute('select * from group_list')
    for row in cur.fetchall():
        print(row)

finally:
    con2.close()


print(a)
