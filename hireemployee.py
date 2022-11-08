from datetime import date
import pickle
import mysql.connector

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def ap1():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    query=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=query.cursor()
    print("-------------Hire Employee Process-------------")

#Employee number
    while True:
        emp_no=input("Enter emp_no (max 5 int): ")
        if len(emp_no) <= 5:
            try:
                emp_no=int(emp_no)
                print("Done OK")
            except ValueError:
                print("emp_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
#Employee Birth date
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
                break
            else:
                if age(birth_date)<20:
                    print("Employee must be atleast 20 years of age!!")
                else:
                    print("Maximum age is 60 years!!!")
                print("\nwrong input\n")
#Employee name          
    while True:
        first_name=input("Enter first name (max 15 char): ")
        if len(first_name)<= 15:
            break
        else:
            print("Max 15 characters")

    while True:
        last_name=input("Enter last name (max 15 char): ")
        if len(last_name)<= 15:
            break
        else:
            print("Max 15 characters")
#Employee Gender
    while True:
        print("1.Male")
        print("2.Female")
        a=input("Enter choice (1 or 2):")
        if a== '1':
            gender='M'
            break
        elif a=='2':
            gender='F'
            break
        else:
            print("Wrong input!!")
#Employee hire date
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
            if age(hire_date)>60:
                print("Employee must be below 60 years of age!!")
            elif age(birth_date)-age(hire_date)>=20:
                break
            else:
                print("Employee must atleast be 20 years of age!!")


    print("=========== Final Data ===========")
    print(emp_no,birth_date,first_name,last_name,gender,hire_date)
    add_employee=("INSERT INTO employees "
    "(emp_no,birth_date,first_name,last_name,gender,hire_date) "
    "VALUES (%s,%s,%s,%s,%s,%s)")
    data_employee=(emp_no,birth_date,first_name,last_name,gender,hire_date)
    try:
        cur.execute(add_employee, data_employee)
        query.commit()
    except mysql.connector.Error as err:
        print(err.msg)
        print("-----------Value addition was unsuccessful!!!!-------------")
    else:
        print("Values added successfully!!")
        while True:
            password=input("Enter employee login password(max 8 characters, min 4): ")
            lp=len(password)
            if lp>8:
                print("Max 8 characters only.")
            elif lp<4:
                print("Minimum 4 characters to be entered.")
            else:
                try:
                    cur.execute("INSERT INTO empass values({},LPAD({},{},'0'))".format(emp_no,password,lp))
                    query.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Password addition was unsuccessful!!!!-------------")
                else:
                    print("Password added successfully!!!")
                    break
    cur.close()
    query.close()