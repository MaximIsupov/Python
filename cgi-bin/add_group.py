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
