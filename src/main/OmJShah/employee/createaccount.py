from tools import dataentering

def ep1(query,cur):
    print("-------------Create account Process-------------")

#client number
    acc_no=dataentering.primary_key_no("acc_no")
#client Birth date
    birth_date=dataentering.birthdate("Client",10,100)
#client name
    first_name,last_name=dataentering.fname(),dataentering.lname()          
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
    password,lp=dataentering.clientpassword()

#mobile no
    mobile_no,lmn=dataentering.mobileno()

#email-id
    email_id=dataentering.email()

    print("=========== Final Data ===========")
    print(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email_id,password)
    add_client=("INSERT INTO clients "
    "(acc_no,type,first_name,last_name,gender,birth_date,accd,mobile_no,email_id,pass) "
    "VALUES (%s,%s,%s,%s,%s,%s,%s,LPAD(%s,%s,'0'),%s,LPAD(%s,%s,'0'))")
    data_client=(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,lmn,email_id,password,lp)
    
    done=dataentering.tableupdate(query,cur,add_client,data_client)
    if done:
        if acc_type=='S':
            bank_balance=dataentering.balance()
            add_savings=("INSERT INTO SAVINGS VALUES(%s,%s,'NO')")
            data_savings=(acc_no,bank_balance)
            done2=dataentering.tableupdate(query,cur,add_savings,data_savings)
            if done2:
                pass
            else:
                print("Unable to add to savings table.")
                print("Deleting from main table.......")
                delete_client=("delete from clients where acc_no = %s")
                data_delete_client=(acc_no)
                done=dataentering.tableupdate(query,cur,delete_client,data_delete_client)
        else:
            bank_balance=dataentering.balance()
            add_current=("INSERT INTO current VALUES(%s,%s,'NO')")
            data_current=(acc_no,bank_balance)
            done2=dataentering.tableupdate(query,cur,add_current,data_current)
            if done2:
                pass
            else:
                print("Unable to add to savings table.")
                print("Deleting from main table.......")
                delete_client=("delete from clients where acc_no = %s")
                data_delete_client=(acc_no)
                done=dataentering.tableupdate(query,cur,delete_client,data_delete_client)

        print("Values added successfully!!")