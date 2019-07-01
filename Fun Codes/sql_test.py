import sqlite3
from datetime import date, datetime
 
# connecting to the database 
connection = sqlite3.connect("Table_new1.db")
#conn = sqlite3.connect("Table_new1.db")
crsr = connection.cursor()
#crsr2 = conn.cursor()
 
# SQL command to create a table in the database
sql_command = """CREATE TABLE IF NOT EXISTS empl_details( 
id INTEGER, 
name VARCHAR(20),
created_at DATE
);"""
 
crsr.execute(sql_command)
#def fun(no,name):
#    today_date = date.today()
#    crsr2.execute("INSERT INTO empl_details VALUES (?,?,?)",(no,name,today_date))
 
def insert(no,name):
    today_date = date.today()
    crsr.execute("INSERT INTO empl_details VALUES (?,?,?)",(no,name,today_date))
    #fun(no,name)
def delete(no):
    crsr.execute("DELETE FROM empl_details WHERE id={}".format(no))

def update(no,name):
    crsr.execute("UPDATE empl_details SET name=? WHERE id=?",(name,no))

def display(first_date,sec_date):
    cursor=crsr.execute("SELECT * from empl_details WHERE created_at BETWEEN ? AND ?",(first_date,sec_date))
    for row in cursor:
        print("ID = ",row[0])
        print("Employee Name = ",row[1])
        print("Created Date = ",row[2])

conti="y"
while(conti=="y"):
    print("1) Insertion")
    print("2) Deletion")
    print("3) Updation")
    print("4) Display")
    option=int(input())
    if(option==1):
        insert(input("Enter ID : "),input("Enter Name : "))
    elif(option==2):
        delete(input("Enter ID to delete : "))
    elif(option==3):
        update(input("Enter ID to update : "),input("Enter Name to update : "))
    elif(option==4):
        display(input("Enter first Date(yyyy-mm-dd) : "),input("Enter second Date(yyyy-mm-dd) : "))
    conti=input("To continue press y : ")

 

connection.commit()
 
connection.close()
