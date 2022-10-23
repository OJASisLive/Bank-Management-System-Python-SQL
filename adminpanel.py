import pickle
import mysql.connector
import hireemployee

def cursor():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    query=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    return query.cursor()

def ap2():
    print("ap2")

def ap3():
    print("ap3")

def ap():
    print("\nWelcome Admin!!")
    
    while True:
        print("\n---------------------Admin Panel-----------------------")
        print("\n1.Hire Employee")
        print("2.Fire Employee")
        print("3.Change employee data")
        print("\nInput 0 to quit.")
        a=input("Enter choice:")
        if a=='1':
            hireemployee.ap1()
        elif a=='2':
            ap2()
        elif a=='3':
            ap3()
        elif a=='0':
            print("Quit Admin Panel.")
            break
        else:
            print("Wrong input!(1,2,3)")