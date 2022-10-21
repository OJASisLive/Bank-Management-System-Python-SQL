import check

import pickle
import mysql.connector


query=""
Password=""
Database=""
def sqlpwd():
    global Password
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Password=dat[0]
    return Password

def sqldb():
    global Database
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Database=dat[1]
    return Database

def connectionquery():
    try:
        Databa=sqldb()
        Passwo=sqlpwd()
        query=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    except:
        import traceback
        traceback.print_exc()
        query=""
    return query

def querycheck():
    conn=connectionquery()
    ans=False
    if conn!="":
        if conn.is_connected:
            print("Connection established successfully.")
            with open("firsttime.txt","w") as f:
                f.write("False")
                ans=True
        
    if not ans:
        print("There was a problem in connection")
        print("Maybe this is because you entered wrong credentials(password and database name)")
    return ans

def mysqlsetup():
    print("\n-----------------MYSQL Setup-------------------\n")
    print("Remember that you can't change the database afterwards\n")
    print("Create a database in your MYSQL Workbench.\n")
    Database=input("Enter database name: ")
    Password=input("Enter sql password (enter '' if nothing):")
    cred2= open("cred.dat","wb")
    data=[Password,Database]
    pickle.dump(data,cred2)
    cred2.close()
    querycheck()

def setup():
    while check.check():
        print("\n\n-----------------Welcome to the Project!!!-------------------")
        print("This is the setup process which runs when the user uses the program for the first time.")
        print("\n----------------------Database Setup------------------------\n")
        print("1.Mysql 8.0 (Dependency MYSQL)")
        print("2.Standalone (Data files)")
        print("0.Cancel operation\n")
        ans2=input("How do you want to store the data? (1/2): ")
        if ans2 == "0":
            break
        if ans2=="1":
            mysqlsetup()
        if ans2=="2":
            print("\nThis is under development :). Please use mysql till then...")
        elif ans2 != "1" or ans2 != "2":
            print("\nWrong input, (1/2).........")
    else: 
        if querycheck():
            connectionquery()
setup()
