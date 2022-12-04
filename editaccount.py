import pickle
import mysql.connector

from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
acc_no=0
acc_creation_date=None
birth_date=None
def ep2(conn,cur):
    while True:
        acc_no=input("Enter acc_no (max 5 int) to edit details: ")
        if len(acc_no) <= 5:
            try:
                acc_no=int(acc_no)
                print("Done OK")
            except ValueError:
                print("acc_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")