from tools import dataentering
def cp2(conn,cur,acc_type,acc_no):
    cur.execute("select cash_in_hand from cash_in_hand where acc_no={}".format(acc_no))
    cash_in_hand=cur.fetchall()
    if cash_in_hand==[]:
        query="insert into cash_in_hand values(%s,0)"
        data=(acc_no,)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            cash_in_hand=0
        else:
            print("Unable to figure out your cash in hand values.")
    else:
        cash_in_hand=cash_in_hand[0][0]
    
    deposit_amt=dataentering.amounts("deposit",cash_in_hand,acc_type)
    if deposit_amt:
        query2="update {} set balance = balance+{} where acc_no = %s".format(acc_type,deposit_amt)
        data2=(acc_no,)
        done2=dataentering.tableupdate(conn,cur,query2,data2)
        if done2:
            query3="update cash_in_hand set cash_in_hand = cash_in_hand-%s where acc_no = %s"
            data3=(cash_in_hand,acc_no)
            done3=dataentering.tableupdate(conn,cur,query3,data3)
            if done3:
                print("Deposit of {} currency successful".format(deposit_amt))
                print()
            else:
                query2="update {} set balance = balance-{} where acc_no = %s".format(acc_type,deposit_amt)
                data2=(acc_no,)
                done2=dataentering.tableupdate(conn,cur,query2,data2)
                if done2:
                    print("Unable to subtract amount from cash_in_hand\n")
        else:
            print("Error while trying to add amount to balance.\n")
    else: 
        pass