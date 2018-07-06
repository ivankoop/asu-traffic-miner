import MySQLdb
import time
from pprint import pprint
from config import DB_USER
from config import DB_PASS
from config import DB_NAME


db = MySQLdb.connect(host="localhost",
                     user=DB_USER,
                     passwd=DB_PASS,
                     db=DB_NAME)


def insert_data(name,value):

    datetime = time.strftime('%Y-%m-%d %H:%M:%S')

    cur = db.cursor()

    cur.execute ("INSERT INTO duration_info (created_at,name,value) VALUES ('%s','%s','%s')" % (datetime,name,value))

    db.commit()
    cur.close()
