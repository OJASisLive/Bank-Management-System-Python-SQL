import createaccount

def ep(conn,cur):
    print("\nWelcome employee!!")
    print("Please log in with your creds (emp_id and password):")

    while True:
        print("---------------------Employee Panel--------------------")
        print("1.Employee login.")
        print("2.Quit.")
        ch = input("Enter your choice:")
        if ch == "1":
            print("------------login panel-------------")
        elif ch == "2":
            cur.close()
            conn.close()
            break
        else:
            print("Wrong input!!!(1 or 2 only)")
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
                a=input("Enter your password:")
                if a==password:
                    choice=menu(emp_no,cur)
                    if choice=="1":
                        createaccount.ep1(conn,cur)
                    elif choice=="2":
                        break
                    elif choice=="3":
                        break
                    elif choice=="4":
                        break
                    elif choice=="0":
                        cur.close()
                        conn.close()
                        break
                    else:
                        print("Wrong input!")
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