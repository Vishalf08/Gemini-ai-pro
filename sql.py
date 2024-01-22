import sqlite3
connection=sqlite3.connect('Emp.db')
cursor=connection.cursor()

table_info="""
Create table Emp(Emp_id int,Name varchar(10),Department varchar(10),Salary int)"""
cursor.execute(table_info)

cursor.execute('''insert into Emp values('100','Vishal','Data Analyst',100000)''')
cursor.execute('''insert into Emp values('101','John','Data Engineer',150000)''')
cursor.execute('''insert into Emp values('102','Rocky','Data Analyst',90000)''')
cursor.execute('''insert into Emp values('103','Jogi','IT Analyst',80000)''')
cursor.execute('''insert into Emp values('104','Tony','Data Analyst',95000)''')
cursor.execute('''insert into Emp values('105','Raju','Data Engineer',80000)''')
cursor.execute('''insert into Emp values('106','Golu','Data Analyst',83000)''')
cursor.execute('''insert into Emp values('107','Nandu','IT Analyst',53000)''')
cursor.execute('''insert into Emp values('108','Tatu','IT Analyst',73000)''')
cursor.execute('''insert into Emp values('109','Bhopendra','Data Analyst',85000)''')

data=cursor.execute('''Select * from Emp''')
for i in data:
      print(i)

connection.commit()
connection.close()
