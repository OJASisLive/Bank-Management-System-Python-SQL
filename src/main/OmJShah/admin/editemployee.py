import mysql.connector
from datetime import date
from tools import dataentering

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
emp_no=0
hire_date=None
birth_date=None
def ap3(conn,cur):
    global emp_no
    global birth_date
    global hire_date
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
        print(results)
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
    global emp_no
    global birth_date
    global hire_date
    print("0 to quit.")
    a=input("What would you like to change from the above:")
    if a == '1':
        en=dataentering.primary_key_no("emp_no")
        try:
            cur.execute("update employees set emp_no={} where emp_no={}".format(en,emp_no))
            conn.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            print("-----------Value addition was unsuccessful!!!!-------------")
        else:
            print("Updated employee number...")

    if a == '2':
        birth_date=dataentering.birthdate("employee",20,60)
        if age(birth_date)-age(hire_date)>=20:
            try:
                cur.execute("update employees set birth_date='{}' where emp_no={}".format(birth_date,emp_no))
                conn.commit()
            except mysql.connector.Error as err:
                print(err.msg)
                print("-----------Value addition was unsuccessful!!!!-------------")
            else:
                print("Updated birth date...")
        else:
            print("Employee must be atleast 20 years of age when hired!!")
            print(birth_date,": birth_date")
            print(hire_date,":hire date you entered")

    if a == '3':
        while True:
            first_name=input("Enter first name (max 15 char): ")
            if len(first_name)<= 15:
                try:
                    cur.execute("update employees set first_name='{}' where emp_no={}".format(first_name,emp_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated first name...")
                    break
            else:
                print("Max 15 characters")

    if a == '4':
        while True:
            last_name=input("Enter last name (max 15 char): ")
            if len(last_name)<= 15:
                try:
                    cur.execute("update employees set last_name='{}' where emp_no={}".format(last_name,emp_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated last name...")
                    break
            else:
                print("Max 15 characters")
    if a == '5':
        while True:
            print("1.Male")
            print("2.Female")
            a=input("Enter choice (1 or 2):")
            if a== '1':
                try:
                    cur.execute("update employees set gender='M' where emp_no={}".format(emp_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated gender...")
                    break
                
            elif a=='2':
                gender='F'
                try:
                    cur.execute("update employees set gender='F' where emp_no={}".format(emp_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated gender...")
                    break

            else:
                print("Wrong input!!")

    if a == '6':
        hire_date=dataentering.date2("employee",birth_date,"hire",20,60)
        try:
            cur.execute("update employees set hire_date='{}' where emp_no={}".format(hire_date,emp_no))
            conn.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            print("-----------Value addition was unsuccessful!!!!-------------")
        else:
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
                    try:
                        cur.execute("UPDATE empass set pass=LPAD({},{},'0') where emp_no={}".format(password,lp,emp_no))
                        conn.commit()
                    except mysql.connector.Error as err:
                        print(err.msg)
                        print("-----------Password change was unsuccessful!!!!-------------")
                    else:
                        print("Password changed successfully!!!")
                        break