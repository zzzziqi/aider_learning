import sqlite3
from sqlite3 import Error

def create_users_table():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('db.sqlite') # create a database connection to a SQLite database
        print(sqlite3.version)
        create_users_table()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_user(username, password):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def user_exists(username, password):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    rows = cur.fetchall()
    conn.close()
    return len(rows) > 0
