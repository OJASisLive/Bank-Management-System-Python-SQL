from tools import dataentering
def cp3(conn,cur,acc_type,acc_no):
    cur.execute("select balance from {} where acc_no={}".format(acc_type,acc_no))
    balance=cur.fetchall()
    balance=balance[0][0]
    withdraw_amt=dataentering.amounts("withdraw",balance,acc_type)
    withdraw_amt=withdraw_amt[0]
    if withdraw_amt:
        query="update {} set balance = balance-%s where acc_no=%s".format(acc_type)
        data=(withdraw_amt,acc_no)
        done=dataentering.tableupdate(conn,cur,query,data)
        if done:
            query2="update cash_in_hand set cash_in_hand=cash_in_hand+%s where acc_no=%s"
            data2=(withdraw_amt,acc_no)
            done2=dataentering.tableupdate(conn,cur,query2,data2)
            if done2:
                print("Successfully withdrawn {} currency".format(withdraw_amt))
                print()
            else:
                query="update {} set balance = balance+%s where acc_no=%s".format(acc_type)
                data=(withdraw_amt,acc_no)
                done=dataentering.tableupdate(conn,cur,query,data)
                if done:
                    print("Couldn't remove money from cash_in_hand\n")
        else:
            print("couldn't update balance\n")
    else:
        print("Couldn't withdraw amount\n")