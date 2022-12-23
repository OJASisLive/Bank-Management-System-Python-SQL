from tools import dataentering
import mysql.connector

def ep1(query,cur):
    print("-------------Create account Process-------------")

#client number
    acc_no=dataentering.primary_key_no("acc_no")
#client Birth date
    birth_date=dataentering.birthdate("Client",10,100)
#client name
    first_name,last_name=dataentering.name()          
#client Gender
    gender=dataentering.gender()
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
    acc_creation_date=dataentering.date2("client",birth_date,"account_creation",10,100)
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
    "(acc_no,type,first_name,last_name,gender,birth_date,accd,mobile_no,email_id,pass) "
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