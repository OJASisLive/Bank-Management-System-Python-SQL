from tools import dataentering
def cp4(conn,cur,acc_type,acc_no):
    rc=input("Enter redeem code: ")
    if rc=="TESTREDEEMCODE":
        query="update {} set balance = balance+%s where acc_no = %s".format(acc_type)
        data=(5000,acc_no)
        done = dataentering.tableupdate(conn,cur,query,data)
        if done:
            print("Added 5000 currency to your account!!")
        else:
            print("There was a problem while processing the request")
    else:
        print("Sorry! This redeem code doesn't work")