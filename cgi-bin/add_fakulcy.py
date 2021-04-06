#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("fakulcy_name", "не задано")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("insert into fakulcies values(?)", (name, ))

conn.commit()
cursor.close()
conn.close()