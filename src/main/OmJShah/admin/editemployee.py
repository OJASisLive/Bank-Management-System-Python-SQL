from datetime import date
from tools import dataentering

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
emp_no=None
hire_date=None
birth_date=None

def ap3(conn,cur):
    global emp_no,birth_date,hire_date
    print("---------Edit employee process----------\n")
    while True:
        print("input ~ to quit")
        emp_no=input(("Enter emp_no of the employee to edit the details: "))
        if emp_no=="~": break
        if len(emp_no) <= 5:
            try:
                emp_no=int(emp_no)
                print("Checking...")
            except ValueError:
                print("emp_no should be an integer!!")
            else:
                next(conn,cur)
                break
        else:
            print("Maximum length is 5!")

def next(conn,cur):
    cur.execute("select * from employees where emp_no={}".format(emp_no))
    results=cur.fetchall()
    if len(results)==0:
        print("That employee number does not exist.")
    else:
        results1=results[0]
        print("1.emp_no:",results1[0])
        print("2.birth_date:",results1[1])
        print("3.first_name:",results1[2])
        print("4.last-name:",results1[3])
        print("5.gender:",results1[4])
        print("6.hire_date:",results1[5])
        print("7.password")
        birth_date=results1[1]
        hire_date=results1[5]
        f2(conn,cur)

def f2(conn,cur):
    global emp_no,birth_date,hire_date
    print("0 to quit.")
    a=input("What would you like to change from the above:")
    if a == '1':
        en=dataentering.primary_key_no("emp_no")
        query="update employees set emp_no=%s where emp_no=%s"
        query2="update empass set emp_no=%s where emp_no=%s"
        data=(en,emp_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            done=dataentering.tableupdate(conn,cur,query2,data)
            if done:
                print("Updated employee number...")

    if a == '2':
        birth_date=dataentering.birthdate("employee",20,60)
        if age(birth_date)-age(hire_date)>=20:
            query="update employees set birth_date=%s where emp_no=%s"
            data=(birth_date,emp_no)
            done=dataentering.tableupdate(conn,cur,query,data)
            if done:
                print("Updated birth date")
        else:
            print("Employee must be atleast 20 years of age when hired!!")
            print(birth_date,": birth_date")
            print(hire_date,":hire date you entered")

    if a == '3':
        first_name=dataentering.fname()
        query="update employees set first_name=%s where emp_no=%s"
        data=(first_name,emp_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated first name...")

    if a == '4':
        last_name=dataentering.lname()
        query="update employees set last_name=%s where emp_no=%s"
        data=(last_name,emp_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated last name...")
                    
    if a == '5':
        gender=dataentering.gender()
        query="update employees set gender=%s where emp_no=%s"
        data=(gender,emp_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated gender...")

    if a == '6':
        hire_date=dataentering.date2("employee",birth_date,"hire",20,60)
        query="update employees set hire_date=%s where emp_no=%s"
        data=(hire_date,emp_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated hire date...")

    if a=='7':
        print("1.Show the password")
        print("2.Change the password")
        ans=input("Enter your choice (1,2):")
        if ans=='1':
            cur.execute("SELECT pass from empass where emp_no={}".format(emp_no))
            result=cur.fetchall()
            print(result[0][0], "is the password.")
        elif ans=='2':
            while True:
                password=input("Enter employee login password(max 8 characters, min 4): ")
                lp=len(password)
                if lp>8:
                    print("Max 8 characters only.")
                elif lp<4:
                    print("Minimum 4 characters to be entered.")
                else:
                    query="UPDATE empass set pass=LPAD(%s,%s,'0') where emp_no=%s"
                    data=(password,lp,emp_no)
                    done=dataentering.tableupdate(conn,cur,query,data)
                    if done:
                        print("Password changed successfully!!!")
                        break
                    else:
                        break