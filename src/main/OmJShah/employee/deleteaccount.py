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
            first_name=results1[2]
            last_name=results1[3]
            print(first_name,last_name,"found.")
            print(" Y - Deletes the account")
            print(" N - Cancel process")
            print("It's case sensitive")
            choice=input("Do you really wish to delete the account of {} {}: ".format(first_name,last_name))
            if choice == "Y":
                query="delete from clients where acc_no = %s"
                data=(acc_no,)
                done=dataentering.tableupdate(conn,cur,query,data)
                if done:
                    print("Deleted {} {}'s account.".format(first_name,last_name))
                    break
                else:
                    print("Deletion was unsuccessful")
            else:
                break
