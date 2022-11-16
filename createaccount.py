import pickle
from datetime import date

import mysql.connector


def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def ep1():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    query=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=query.cursor()
    print("-------------Create account Process-------------")

#client number
    while True:
        acc_no=input("Enter acc_no (max 5 int): ")
        if len(acc_no) <= 5:
            try:
                acc_no=int(acc_no)
                print("Done OK")
            except ValueError:
                print("acc_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
#client Birth date
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
            if age(birth_date)>=10:
                break
            else:
                print("Account holder must be atleast 10 years of age!!")
#client name          
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
#client Gender
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

#client Account Type
    while True:
        print("1.Savings account")
        print("2.Current account")
        a=input("Enter choice (1 or 2):")
        if a== '1':
            acc_type='S'
            break
        elif a=='2':
            acc_type='C'
            break
        else:
            print("Wrong input!!")

#Account creation date
    while True:
        while True:
            hyear=input("Enter account_creation year (4 int): ")
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
            hmonth=input("Enter account_creation month (2 int) (01 to 12): ")
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
            hday=input("Enter account_creation day (2 int) (01 to 31): ")
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
            acc_creation_date=date(hyear,hmonth,hday)
        except ValueError:
            import traceback
            traceback.print_exc()
        else:
            if age(birth_date)-age(acc_creation_date)>=10:
                break
            else:
                print("client must atleast be 10 years of age!!")
#client password/pin
    while True:
            password=input("Enter client login password(max 8 characters, min 4): ")
            lp=len(password)
            if lp>8:
                print("Max 8 characters only.")
            elif lp<4:
                print("Minimum 4 characters to be entered.")
            else:
                break

#mobile no
    while True:
        mobile_no_str=input("Enter mobile no. (7 to 15 int)") 
        mobile_no=mobile_no_str 
        #Thanks to the international phone numbering plan (ITU-T E. 164), 
        #phone numbers cannot contain more than 15 digits. The shortest 
        #international phone numbers in use contain seven digits.
        try:
            mobile_no=int(mobile_no)
        except ValueError:
            print("acc_no should be an integer!!")
        else:
            if len(mobile_no_str)>6 and len(mobile_no_str)<16:
                mobile_no=mobile_no_str
                lmn=len(mobile_no)
                break
            else:
                print("Mobile number can have min 7 digits and max 15!!")

#email-id
    while True:
        email_id=input("Enter client Email ID (max 25 char):")
        if len(email_id)<26:
            break
        else:
            print("Maximum 25 characters")

    

    print("=========== Final Data ===========")
    print(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email_id,password)
    add_client=("INSERT INTO clients "
    "(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email_id,pass) "
    "VALUES (%s,%s,%s,%s,%s,%s,%s,LPAD(%s,%s,'0'),%s,LPAD(%s,%s,'0'))")
    data_client=(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,lmn,email_id,password,lp)
    try:
        cur.execute(add_client, data_client)
        query.commit()
    except mysql.connector.Error as err:
        print(err.msg)
        print("-----------Value addition was unsuccessful!!!!-------------")
    else:
        print("Values added successfully!!")
    cur.close()
    query.close()