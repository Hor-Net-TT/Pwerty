import sqlite3

connect = sqlite3.connect('db.db')
cursor = connect.cursor()


def start():
    cursor.execute('''CREATE TABLE IF NOT EXISTS User(
        Id INT PRIMARY KEY,
        Lang TEXT DEFAULT 'RUS'
    )''')
    connect.commit()

def new(user):
    cursor.execute('''INSERT INTO User VALUES (?, ?)''')