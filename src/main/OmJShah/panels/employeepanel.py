from employee import createaccount
from employee import editaccount
from employee import deleteaccount
from employee import showaccounts

def ep(conn,cur):
    print("\nWelcome employee!!")
    print("Please log in with your creds (emp_id and password):")
    print("---------------------Employee Panel--------------------")
    print("1.Employee login.")
    print("2.Quit.")
    ch = input("Enter your choice:")
    logged_in= bool(False)
    if ch == "1":
        print("------------login panel-------------")
        logged_in=bool(True)
    elif ch == "2":
        pass
    else:
        print("Wrong input!!!(1 or 2 only)")
    if logged_in:
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

        cur.execute("select * from empass where emp_no = {}".format(emp_no))
        record=cur.fetchall()
        if record == []:
            print("This emp_no doesn't exist!!!")
        else:
            while True:
                password=record[0][1]
                print("\nInput ~ to quit.")
                a=input("Enter your password to continue:")
                print()
                if a==password:
                    choice=menu(emp_no,cur)
                    if choice=="1":
                        createaccount.ep1(conn,cur)
                    elif choice=="2":
                        editaccount.ep2(conn,cur)
                    elif choice=="3":
                        deleteaccount.ep3(conn,cur)
                    elif choice=="4":
                        showaccounts.ep4(cur)
                    elif choice=="0":
                        break
                    else:
                        print("Wrong input!")
                elif a == "~" : break
                else:
                    print("Wrong password!!")
                    break

def menu(x,cur):
    cur.execute("select first_name,last_name from employees where emp_no = {}".format(x))
    record=cur.fetchone()
    print("---------------Welcome {} {} ----------------".format(record[0],record[1]))
    print("1.Create client account")
    print("2.Change client details")
    print("3.Close client account")
    print("4.Show client table")
    print("Enter 0 to quit.")
    choice=input("Enter your choice: ")
    return choice