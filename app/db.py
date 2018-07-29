#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def updateDb(conn):
    cur = conn.cursor()
    new_content = "Requesting 20 blankets"
    user_id = 2
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id))
    user_id = 11
    new_content = "I want to donate 3 blankets"
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id))
    user_id = 3
    new_content = "Hi guys! I have couple of extra notebooks that I would like to donate :)"
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id)) 
    user_id = 4
    new_content = "We are SF based non profit, requesting medical supplies"
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id))
    user_id = 5
    new_content = "I want to donate a couple of bedsheets"
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id))
    user_id = 14
    new_content = "I have homemade baked pies that I would like to share"
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id))
    user_id = 12
    new_content = "We are looking for grocery supplies"
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id))
    user_id = 6
    new_content = "I would like to volunteer few hours on Sunday"
    cur.execute("UPDATE post SET content = ?  WHERE user_id= ? ",
  (new_content,user_id))
   
   
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM post")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM post")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    database = 'social.db'
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        #select_all_tasks(conn)
        updateDb(conn) 
        cur = conn.cursor()
	print 'here'
        cur.execute("SELECT user_id FROM post")
	rows = cur.fetchall()
	for r in rows:
		print r
	print 'next'
        select_all_tasks(conn)
 
if __name__ == '__main__':
    main()
