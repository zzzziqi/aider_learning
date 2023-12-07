import sqlite3
from sqlite3 import Error

def create_users_table():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT, password TEXT)")
    conn.commit()
    conn.close()

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('db.sqlite') # create a database connection to a SQLite database
        create_users_table()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_user(username, email, password):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

def user_exists(username_or_email, password):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE (username = ? OR email = ?) AND password = ?", (username_or_email, username_or_email, password))
    rows = cur.fetchall()
    conn.close()
    return len(rows) > 0

def user_exists_by_name(username):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    rows = cur.fetchall()
    conn.close()
    return len(rows) > 0

def get_all_users():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows
