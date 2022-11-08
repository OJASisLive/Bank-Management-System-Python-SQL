import mysql.connector
import pickle
def ap4():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()
    cur.execute("select * from employees")
    results=cur.fetchall()
    print("+---------+-------------+------------------+------------------+---------+-------------+")
    print("|","%7s"%"EMP_NO","|","%11s"%"BIRTH_DATE","|","%16s"%"FIRST_NAME","|","%16s"%"LAST_NAME","|","%7s"%"GENDER","|","%11s"%"HIRE_DATE","|")
    for row in results:
        print("+---------+-------------+------------------+------------------+---------+-------------+")
        print("|","%7s"%row[0],"|","%11s"%row[1],"|","%16s"%row[2],"|","%16s"%row[3],"|","%7s"%row[4],"|","%11s"%row[5],"|")
    cur.close()
    conn.close()
    print("+---------+-------------+------------------+------------------+---------+-------------+")