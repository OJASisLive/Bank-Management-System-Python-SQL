from datetime import date
from tools import dataentering

acc_no=None
first_name=None
last_name=None
gender=None
birth_date=None
acc_creation_date=None
mobile_no=None
email_id=None
password = None

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def ep2(conn,cur):
    global acc_no,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email_id,password
    while True:
        print("\ninput ~ to quit")
        acc_no=input("Enter acc_no (max 5 int) to edit details: ")
        if acc_no=="~": break
        elif len(acc_no) <= 5:
            try:
                acc_no=int(acc_no)
                print("Done OK")
            except ValueError:
                print("acc_no should be an integer!!")
        else:
            print("Maximum length is 5!")
        cur.execute("select * from clients where acc_no={}".format(acc_no))
        results=cur.fetchall()
        if len(results)==0:
            print("That account number does not exist.")
        else:
            results1=results[0]
            first_name=results1[2]
            last_name=results1[3]
            gender=results1[4]
            birth_date=results1[5]
            acc_creation_date=results1[6]
            mobile_no=results1[7]
            email_id=results1[8]
            password=results1[9]

            print("1. first_name            = ",first_name)
            print("2. last_name             = ",last_name)
            print("3. gender                = ",gender)
            print("4. birth_date            = ",birth_date)
            print("5. account_creation_date = ",acc_creation_date)
            print("6. mobile_no             = ",mobile_no)
            print("7. email_id              = ",email_id)
            print("8. password")
            print("0 to quit")
            ep2f2(conn,cur)
    
def ep2f2(conn,cur):
    global acc_no,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email_id,password
    choice=input("What would you like to change from here: ")
#First-name    
    if choice == "1":
        first_name=dataentering.fname()
        query="update clients set first_name=%s where acc_no=%s"
        data=(first_name,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated first name")

#Last-name
    elif choice == "2":
        last_name=dataentering.lname()
        query="update clients set last_name=%s where acc_no=%s"
        data=(last_name,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated last name")

#Gender
    elif choice == "3":
        gender=dataentering.gender()
        query="update clients set gender=%s where acc_no=%s"
        data=(gender,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated gender")

#Birth-date
    elif choice == "4":
        birth_date=dataentering.birthdate("Client",10,100)
        if age(birth_date)-age(acc_creation_date)>=10:
            query="update clients set birth_date=%s where acc_no=%s"
            data=(birth_date,acc_no)
            done=dataentering.tableupdate(conn,cur,query,data)
            if done:
                print("Updated birth date")
        else:
            print("The client should atleast be 10 years of age.")
            print("Birth date:",birth_date)
            print("Account Creation Date:",acc_creation_date)

#Account-creation-date(accd)
    elif choice == "5":
        acc_creation_date=dataentering.date2("client",birth_date,"account_creation",10,100)
        query="update clients set accd=%s where acc_no=%s"
        data=(acc_creation_date,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated account creation date")

#Mobile No
    elif choice == "6":
        mobile_no,lmn=dataentering.mobileno()
        query="update clients set mobile_no=LPAD(%s,%s,'0') where acc_no=%s"
        data=(mobile_no,lmn,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated mobile number")

#Email ID
    elif choice == "7":
        email_id=dataentering.email()
        query="update clients set email=%s where acc_no=%s"
        data=(mobile_no,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Updated mobile number")
#Password
    elif choice == "8":
        while True:
            print("1.Show Password")
            print("2.Change Password")
            print("0 to quit")
            choice=input("Enter choice: ")
            if choice == "1":
                print("\nThe password will be printed on the next line")
                print(password)
                print()
            elif choice == "2":
                password,lp=dataentering.clientpassword()
                query="update clients set pass=LPAD(%s,%s,'0') where acc_no=%s"
                data=(password,lp,acc_no)
                done=dataentering.tableupdate(conn,cur,query,data)
                if done:
                    print("Updated password")
            elif choice == "0":
                break
            else:
                print("Wrong input!!")
    elif choice == "0":
        pass
    else:
        print("Wrong input!!")