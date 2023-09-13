import sqlite3

conn = sqlite3.connect('typefaster.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE users (username TEXT, password_hash TEXT)')
print("Created table successfully!")

conn.close()