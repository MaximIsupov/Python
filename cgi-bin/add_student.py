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

cursor.execute("select * from students")
studs = cursor.fetchall()

cursor.execute("select * from groups")
grou = cursor.fetchall()

cursor.execute("select * from fakulcies")
faks = cursor.fetchall()

print("Content-type: text/html")
print()
print("<h1> Студенты: </h1>")
for line in studs:
    print("<div>")
    for el in line:
        print(el, " ", end='')
    print("</div>")

print()
print("<h1> Группы: </h1>")
for line in grou:
    print("<div>")
    for el in line:
        print(el, " ", end='')
    print("</div>")

print("<h1> Факультеты: </h1>")
for line in faks:
    print("<div>")
    for el in line:
        print(el, " ", end='')
    print("</div>")

conn.commit()
cursor.close()
conn.close()



