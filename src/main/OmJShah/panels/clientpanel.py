from tools import dataentering
def cp(conn,cur):
    print("\n------------------Client Panel------------------")
    print("Welcome client!!")
    acc_no=dataentering.primary_key_no("acc_no")
    cur.execute("select first_name,last_name,pass,type from clients where acc_no = {}".format(acc_no))
    result=cur.fetchall()
    if result == []:
        print("No account holder with this account number.")
    else:
        acc_type=result[0][3]
        if acc_type == 'S': acc_type="savings"
        if acc_type == 'C': acc_type="current"
        while True:
            print("\nInput ~ to quit")
            passwd=input("Enter password to continue: ")
            if passwd == "~":
                break
            elif passwd == result[0][2]:
                print("\n--------------------Welcome {} {}-------------------".format(result[0][0],result[0][1]))
                cmenu(conn,cur,acc_no,acc_type)
            else:
                print("Wrong password")
            
def cmenu(conn,cur,acc_no,acc_type):
    print("1.Show Balance")
    print("2.Deposit money")
    print("3.Withdraw money")
    if acc_type=='savings':
        print("4.Ask for loan")
        print("5.Check loan status")
    else:
        print("4.Check overdraft status")
    print("~ to quit")
    choice=input("Enter your choice: ")
    if choice=="~": pass
    elif choice=="1":
        cur.execute("select balance from {} where acc_no={}".format(acc_type,acc_no))
        balance=cur.fetchall()
        print("Your balance is: ",balance[0][0])
        print()
    elif choice=="2":
        pass
    elif choice=="3":
        pass
    elif choice=="4":
        pass
    elif choice=="5":
        pass
    else:
        print("Wrong input!!!!\n")
