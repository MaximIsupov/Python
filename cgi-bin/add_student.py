#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
idd = form.getfirst("id", "не задано")
name = form.getfirst("name", "не задано")
surname = form.getfirst("surname", "не задано")
group = form.getfirst("group", "не задано")

print(idd, name, surname, group)

students = (int(idd), str(name), str(surname), str(group))

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("insert into students values(?, ?, ?, ?)", students)

conn.commit()
cursor.close()
conn.close()


