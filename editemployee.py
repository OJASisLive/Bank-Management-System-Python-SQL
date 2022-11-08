import mysql.connector
import pickle
from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

cur=None
conn=None
emp_no=0
hire_date=None
birth_date=None
def ap3():
    global cur
    global conn
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()

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
        f2()

def f2():
    global cur
    global conn
    global emp_no
    global birth_date
    global hire_date
    print("0 to quit.")
    a=input("What would you like to change from the above:")
    if a == '1':
        while True:
            en=input("Enter emp_no (max 5 int): ")
            if len(en) <= 5:
                try:
                    en=int(en)
                    print("Done OK")
                except ValueError:
                    print("emp_no should be an integer!!")
                else:
                    try:
                        cur.execute("update employees set emp_no={} where emp_no={}".format(en,emp_no))
                        conn.commit()
                    except mysql.connector.Error as err:
                        print(err.msg)
                        print("-----------Value addition was unsuccessful!!!!-------------")
                    else:
                        print("Updated employee number...")
                        break
            else:
                print("Maximum length is 5!")
    if a == '2':
        while True:
            while True:
                year=input("Enter birth year (4 int): ")
                if len(year) == 4:
                    try:
                        year=int(year)
                        print("Done OK")
                    except ValueError:
                        print("year should be an integer!!")
                    else:
                        break
                else:
                    print("Year consists of 4 integers!!")

            while True:
                month=input("Enter birth month (2 int) (01 to 12): ")
                if len(month) == 2:
                    try:
                        month=int(month)
                        print("Done OK")
                    except ValueError:
                        print("month should be an integer!!")
                    else:
                        break
                else:
                    print("Month consists of 2 integers!!")

            while True:
                day=input("Enter birth day (2 int) : ")
                if len(day) == 2:
                    try:
                        day=int(day)
                        print("Done OK")
                    except ValueError:
                        print("Date should be an integer!!")
                    else:
                        break
                else:
                    print("Date consists of 2 integers!!")

            try:
                birth_date=date(year,month,day)
            except ValueError:
                import traceback
                traceback.print_exc()
            else:
                if age(birth_date)>=20 and age(birth_date)<=60:
                    if age(birth_date)-age(hire_date)>=20:
                        try:
                            cur.execute("update employees set birth_date='{}' where emp_no={}".format(birth_date,emp_no))
                            conn.commit()
                        except mysql.connector.Error as err:
                            print(err.msg)
                            print("-----------Value addition was unsuccessful!!!!-------------")
                            break
                        else:
                            print("Updated birth date...")
                            break
                    else:
                        print("Employee must be atleast 20 years of age when hired!!")
                        print(birth_date,": birth_date")
                        print(hire_date,":hire date you entered")
                else:
                    if age(birth_date)<20:
                        print("Employee must be atleast 20 years of age!!")
                    else:
                        print("Maximum age is 60 years!!!")
                    print("\nwrong input\n")
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
        while True:
            while True:
                hyear=input("Enter hire year (4 int): ")
                if len(hyear) == 4:
                    try:
                        hyear=int(hyear)
                        print("Done OK")
                    except ValueError:
                        print("year should be an integer!!")
                    else:
                        break
                else:
                    print("Year consists of 4 integers!!")

            while True:
                hmonth=input("Enter hire month (2 int) (01 to 12): ")
                if len(hmonth) == 2:
                    try:
                        hmonth=int(hmonth)
                        print("Done OK")
                    except ValueError:
                        print("month should be an integer!!")
                    else:
                        break
                else:
                    print("Month consists of 2 integers!!")

            while True:
                hday=input("Enter hire day (2 int) (01 to 31): ")
                if len(hday) == 2:
                    try:
                        hday=int(hday)
                        print("Done OK")
                    except ValueError:
                        print("Date should be an integer!!")
                    else:
                        break
                else:
                    print("Date consists of 2 integers!!")

            try:
                hire_date=date(hyear,hmonth,hday)
            except ValueError:
                import traceback
                traceback.print_exc()
            else:
                if age(birth_date)-age(hire_date)>=20:
                    try:
                        cur.execute("update employees set hire_date='{}' where emp_no={}".format(hire_date,emp_no))
                        conn.commit()
                    except mysql.connector.Error as err:
                        print(err.msg)
                        print("-----------Value addition was unsuccessful!!!!-------------")
                        break
                    else:
                        print("Updated hire date...")
                        break
                else:
                    print("Employee must atleast be 20 years of age when hired!!")
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
    cur.close()
    conn.close()