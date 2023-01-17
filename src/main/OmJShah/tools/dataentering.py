from datetime import date
import mysql.connector

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def primary_key_no(x):
#Employee number and client number
    while True:
        emp_no=input("Enter {} (max 5 int): ".format(x))
        if len(emp_no) <= 5:
            try:
                emp_no=int(emp_no)
                print("Done OK")
            except ValueError:
                print("{} should be an integer!!".format(x))
            else:
                return emp_no
        else:
            print("Maximum length is 5!")

def birthdate(person,minage,maxage):     
#Employee Birth date and client birth date
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
            if age(birth_date)>=minage and age(birth_date)<=maxage:
                return birth_date
            else:
                if age(birth_date)<minage:
                    print("{} must be atleast {} years of age!!".format(person,minage))
                else:
                    print("Maximum age is {} years!!!".format(maxage))
                print("\nwrong input\n")

def fname():
#Employee name and client name     
    while True:
        first_name=input("Enter first name (max 15 char): ")
        if len(first_name)<= 15:
            break
        else:
            print("Max 15 characters")
    return first_name

def lname():
    while True:
        last_name=input("Enter last name (max 15 char): ")
        if len(last_name)<= 15:
            break
        else:
            print("Max 15 characters")
    
    return last_name

def gender():
#Employee Gender and client gender
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
    return gender

def date2(person,birth_date,hire_or_creation,minage,maxage):
#Employee hire date and account creation date
    while True:
        while True:
            hyear=input("Enter {} year (4 int): ".format(hire_or_creation))
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
            hmonth=input("Enter {} month (2 int) (01 to 12): ".format(hire_or_creation))
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
            hday=input("Enter {} day (2 int) (01 to 31): ".format(hire_or_creation))
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
            if age(hire_date)>maxage:
                print("{} must be below {} years of age!!".format(person,maxage))
            elif age(birth_date)-age(hire_date)>=minage:
                break
            else:
                print("{} must atleast be {} years of age!!".format(person,minage))
    return hire_date

def mobileno():
    while True:
        mobile_no_str=input("Enter mobile no. (7 to 15 int): ") 
        mobile_no=mobile_no_str 
        #Thanks to the international phone numbering plan (ITU-T E. 164), 
        #phone numbers cannot contain more than 15 digits. The shortest 
        #international phone numbers in use contain seven digits.
        try:
            mobile_no=int(mobile_no)
        except ValueError:
            print("mobile_no should be an integer!!")
        else:
            if len(mobile_no_str)>6 and len(mobile_no_str)<16:
                mobile_no=mobile_no_str
                lmn=len(mobile_no)
                break
            else:
                print("Mobile number can have min 7 digits and max 15!!")
    return mobile_no,lmn

def email():
    while True:
        email_id=input("Enter client Email ID (max 25 char): ")
        if len(email_id)<26:
            break
        else:
            print("Maximum 25 characters")
    return email_id

def clientpassword():
    while True:
            password=input("Enter client login password(max 8 characters, min 4): ")
            lp=len(password)
            if lp>8:
                print("Max 8 characters only.")
            elif lp<4:
                print("Minimum 4 characters to be entered.")
            else:
                break
    return password,lp

def tableupdate(conn,cur,query,data):
    try:
        cur.execute(query,data)
        conn.commit()
    except mysql.connector.Error as err:
        print(err.msg)
        print("-----------Value addition/deletion was unsuccessful!!!!-------------")
    else:
        return bool(True)

#bank balance 
def balance():
    while True:
        bank_balance=input("Enter starting balance (min 1000 currency): ")
        if len(bank_balance) >= 3:
            try:
                bank_balance=int(bank_balance)
                print("Done OK")
            except ValueError:
                print("Balance should be an integer!!")
            else:
                if bank_balance>=1000:
                    return bank_balance
        else:
            print("Minimum balance is 1000 currency")

#Withdraw amount and Deposit amount
def amounts(deposit_or_withdraw_or_transfer,cash_in_hand_or_balance,acc_type):
    while True:
        print()
        print("--------------------{} screen-------------------".format(deposit_or_withdraw_or_transfer))
        amt=input("Enter amount to {}: ".format(deposit_or_withdraw_or_transfer))
        try:
            amt=int(amt)
            print("Done OK")
        except ValueError:
            print("{} amount should be an integer!!".format(deposit_or_withdraw_or_transfer))
        else:
            if amt<=cash_in_hand_or_balance:
                return amt,None
            else:
                if deposit_or_withdraw_or_transfer=="transfer":
                    if acc_type=="current":
                        overdraft=amt-cash_in_hand_or_balance
                        if (overdraft) <= 50000:
                            return amt,overdraft
                        else:
                            return bool(False),None
                    else:
                        print("You do not have enough balance\n")
                else:
                    if deposit_or_withdraw_or_transfer=="deposit":
                        print("You do not have sufficient cash_in_hand\n")
                    else:
                        print("You do not have enough balance\n")
                    return bool(False),None

def handcash(conn,cur,acc_no):
    cur.execute("select cash_in_hand from cash_in_hand where acc_no={}".format(acc_no))
    cash_in_hand=cur.fetchall()
    if cash_in_hand==[]:
        query="insert into cash_in_hand values(%s,0)"
        data=(acc_no,)
        done=tableupdate(conn,cur,query,data)
        if done:
            cash_in_hand=0
        else:
            print("Unable to figure out your cash in hand values.")
    else:
        cash_in_hand=cash_in_hand[0][0]
    return cash_in_hand