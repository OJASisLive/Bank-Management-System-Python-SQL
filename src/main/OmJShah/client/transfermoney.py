from tools import dataentering
def cp6(conn,cur,acc_type,acc_no,balance):
    acc_to_transfer=dataentering.primary_key_no("acc_no of receiver")
    cur.execute("select * from clients where acc_no={}".format(acc_to_transfer))
    result=cur.fetchall()
    if result==[]:
        print("That account number doesn't exist\n")
    elif acc_to_transfer==acc_no:
        print("You can't transfer to yourself\n")
    else:
        acc_type_receiver=result[0][1]
        if acc_type_receiver == 'S': acc_type_receiver="savings"
        if acc_type_receiver == 'C': acc_type_receiver="current"
        fname,lname=result[0][2],result[0][3]
        transfer_amt,overdraft=dataentering.amounts("transfer",balance,acc_type)
        print(" Y - Yes")
        print(" N - No")
        ch=input("Do you want transfer {} currency to {} {}'s account: ".format(transfer_amt,fname,lname))
        if ch == "Y" :

            if transfer_amt:
                if acc_type=="current":
                    if overdraft!=None:
                        print('''You will be notified about the overdraft status when an employee
                                sanctions your overdraft...''')
                        #TODO:some more stuff 
                else:
                    query="update {} set balance=balance-%s where acc_no = %s".format(acc_type)
                    data=(transfer_amt,acc_no)
                    done=dataentering.tableupdate(conn,cur,query,data)
                    if done:
                        query2="update {} set balance=balance+%s where acc_no=%s".format(acc_type_receiver)
                        data2=(transfer_amt,acc_to_transfer)
                        done2=dataentering.tableupdate(conn,cur,query2,data2)
                        if done2:
                            print("Successfully transferred {} currency\n".format(transfer_amt))
                        else:
                            query="update {} set balance=balance+%s where acc_no = %s".format(acc_type)
                            data=(transfer_amt,acc_no)
                            done=dataentering.tableupdate(conn,cur,query,data)
                            if done:
                                print("Couldn't update receiver's balance\n")
                    else:
                        print("Couldn't transfer money.")
            else :
                print("You do not have enough balance!!")

        else:
            print("Cancelled transfer")