import mysql.connector
import pickle

cred = open("cred.dat","rb")
dat=pickle.load(cred)
cred.close()
Passwo=dat[0]
Databa=dat[1]
conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
cur=conn.cursor()

def ap3():
    print("---------Edit employee process----------\n")
    while True:
        emp_no=input(("Enter emp_no of the employee to edit the details: "))
        if len(emp_no) <= 5:
            try:
                emp_no=int(emp_no)
                print("Checking...")
            except ValueError:
                print("emp_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
    cur.execute("select * from employees where emp_no={}".format(emp_no))
    results=cur.fetchall()
    if results == []:
        print("That employee number does not exist.")
    else:
        print(results)
ap3()

def f2():
    print("1.emp_no")
    print("2.birth_date")
    print("3.first_name")
    print("4.last-name")
    print("5.gender")
    print("6.hire_date")
    print("0 to quit.")
    a=input("What would you like to change from the above:")