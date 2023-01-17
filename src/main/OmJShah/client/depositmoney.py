from tools import dataentering
def cp2(conn,cur,acc_type,acc_no):
    cash_in_hand=dataentering.handcash(conn,cur,acc_no)
    
    deposit_amt=dataentering.amounts("deposit",cash_in_hand,acc_type)
    deposit_amt=deposit_amt[0]
    if deposit_amt:
        query2="update {} set balance = balance+%s where acc_no = %s".format(acc_type)
        data2=(deposit_amt,acc_no)
        done2=dataentering.tableupdate(conn,cur,query2,data2)
        if done2:
            query3="update cash_in_hand set cash_in_hand = cash_in_hand-%s where acc_no = %s"
            data3=(cash_in_hand,acc_no)
            done3=dataentering.tableupdate(conn,cur,query3,data3)
            if done3:
                print("Deposit of {} currency successful".format(deposit_amt))
                print()
            else:
                query2="update {} set balance = balance-%s where acc_no = %s".format(acc_type)
                data2=(deposit_amt,acc_no)
                done2=dataentering.tableupdate(conn,cur,query2,data2)
                if done2:
                    print("Unable to subtract amount from cash_in_hand\n")
        else:
            print("Error while trying to add amount to balance.\n")
    else: 
        pass