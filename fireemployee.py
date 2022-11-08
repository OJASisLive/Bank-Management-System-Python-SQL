import mysql.connector
import pickle
def ap2():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()
    print("---------Fire employee process----------\n")
    while True:
        emp_no=input(("Enter emp_no of the employee to fire them: "))
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
    
    query="delete from employees where emp_no = {}".format(emp_no)
    query2="delete from empass where emp_no = {}".format(emp_no)
    cur.execute("select emp_no from employees")
    record=cur.fetchall()
    changed=False
    for r in record:
        if r[0]==emp_no:
            try:
                cur.execute(query2)
                conn.commit()
                cur.execute(query)
                conn.commit()
                changed=True
            except mysql.connector.Error as err:
                print(err.msg)
                print("-----------Value deletion was unsuccessful!!!!-------------\n")
            else:
                print("Employee fired successfully...\n")
    if not changed:
        print("The employee number does not exist.")
        print("------------Could not fire employee-----------\n")
    cur.close()
    conn.close()