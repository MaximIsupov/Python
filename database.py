import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
#cursor.execute("create table students(id integer primary key, name varchar, surname varchar, group_name varchar, foreign key(group_name) references groups(group_num))")
#cursor.execute("create table groups(group_num varchar primary key, fakulcy_name varchar, foreign key(fakulcy_name) references fakulcies(name))")
#cursor.execute("create table fakulcies(name varchar primary key)")
#cursor.execute("drop table students")
#cursor.execute("drop table groups")
#cursor.execute("drop table fakulcies")
#cursor.execute("insert into students values(1, 'Maxim', 'Isupov', 35)")
print(list(cursor.execute("select * from students")))
cursor.close()
conn.commit()
conn.close()
