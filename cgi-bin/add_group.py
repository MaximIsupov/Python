#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
group_num = form.getfirst("num", "не задано")
name = form.getfirst("fakulcy_name", "не задано")

groups = (group_num, name)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("insert into groups values(?, ?)", groups)

print()

conn.commit()
cursor.close()
conn.close()