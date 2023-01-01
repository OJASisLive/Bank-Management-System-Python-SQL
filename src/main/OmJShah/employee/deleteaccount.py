from tools import dataentering

acc_no=None
def ep3(conn,cur):
    global acc_no
    while True:
        print("\n----------------Account Deleteion Menu-----------------\n")
        print("input ~ to quit")
        acc_no=input("Enter acc_no (max 5 int) to DELETE THE ACCOUNT: ")
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
        else :
            results1=results[0]
            acc_type=results1[1]
            if acc_type == 'S': 
                loan_or_od="loan"
                acc_type="savings"
            if acc_type == 'C': 
                loan_or_od="overdraft"
                acc_type="current"
            cur.execute("select {} from {} where acc_no={}".format(loan_or_od,acc_type,acc_no))
            status=cur.fetchall()
            status=status[0][0]
            first_name=results1[2]
            last_name=results1[3]
            if status == "YES": 
                print("The Client {} {} has {} money to repay".format(first_name,last_name,loan_or_od))
                print("The account can't be deleted until {} is repayed".format(loan_or_od))
                break
            else:            
                print(first_name,last_name,"found.")
                print(" Y - Deletes the account")
                print(" N - Cancel process")
                print("It's case sensitive")
                choice=input("Do you really wish to delete the account of {} {}: ".format(first_name,last_name))
                if choice == "Y":
                    query="delete from clients where acc_no = %s"
                    data=(acc_no,)
                    query2="delete from {} where acc_no = %s".format(acc_type)
                    data2=(acc_no,)
                    done=dataentering.tableupdate(conn,cur,query,data)
                    if done:
                        done2=dataentering.tableupdate(conn,cur,query2,data2)
                        if done2:
                            print("Deleted {} {}'s account.".format(first_name,last_name))
                            break
                        else:
                            print("Deletion from {} table was unsuccessful".format(acc_type))
                    else:
                        print("Deletion was unsuccessful")
                else:
                    break
