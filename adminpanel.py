from datetime import date
from traceback import format_exc, format_exception

def ap1():
    print("-------------Hire Employee Process-------------")
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

    while True:
        while True:
            year=input("Enter birth year (4 int): ")
            if len(year) == 4:
                try:
                    year=int(year)
                    print("Done OK")
                except ValueError:
                    print("year should be an integer!!")
                else:
                    break
            else:
                print("Year consists of 4 integers!!")

        while True:
            month=input("Enter birth month (2 int) (01 to 12): ")
            if len(month) == 2:
                try:
                    month=int(month)
                    print("Done OK")
                except ValueError:
                    print("month should be an integer!!")
                else:
                    break
            else:
                print("Month consists of 2 integers!!")

        while True:
            day=input("Enter birth day (2 int) : ")
            if len(day) == 2:
                try:
                    day=int(day)
                    print("Done OK")
                except ValueError:
                    print("Date should be an integer!!")
                else:
                    break
            else:
                print("Date consists of 2 integers!!")

        try:
            birth_date=date(year,month,day)
            break
        except ValueError:
            import traceback
            traceback.print_exc
            
    while True:
        first_name=input("Enter first name (max 15 char)")
        if len(first_name)<= 15:
            break
        else:
            print("Max 15 characters")

    while True:
        last_name=input("Enter last name (max 15 char)")
        if len(last_name)<= 15:
            break
        else:
            print("Max 15 characters")

    while True:
        print("1.Male")
        print("2.Female")
        a=input("Enter choice (1 or 2):")
        if a== '1':
            gender='M'
            break
        elif a=='2':
            gender='F'
            break
        else:
            print("Wrong input!!")

    while True:
        while True:
            hyear=input("Enter hire year (4 int): ")
            if len(hyear) == 4:
                try:
                    hyear=int(hyear)
                    print("Done OK")
                except ValueError:
                    print("year should be an integer!!")
                else:
                    break
            else:
                print("Year consists of 4 integers!!")

        while True:
            hmonth=input("Enter hire month (2 int) (01 to 12): ")
            if len(hmonth) == 2:
                try:
                    hmonth=int(hmonth)
                    print("Done OK")
                except ValueError:
                    print("month should be an integer!!")
                else:
                    break
            else:
                print("Month consists of 2 integers!!")

        while True:
            hday=input("Enter hire day (2 int) (01 to 31): ")
            if len(hday) == 2:
                try:
                    hday=int(hday)
                    print("Done OK")
                except ValueError:
                    print("Date should be an integer!!")
                else:
                    break
            else:
                print("Date consists of 2 integers!!")

        try:
            hire_date=date(hyear,hmonth,hday)
            break
        except ValueError:
            import traceback
            traceback.print_exc

    while True:
        age=input("Enter employee age:")
        if len(age) == 2:
            try:
                age=int(age)
                print("Done OK")
            except ValueError:
                print("Age should be an integer!!")
            else:
                break
        else:
            print("Age consists of 2 integers!!")

    print("=========== Final Data ===========\n")
    print(emp_no,
    birth_date,
    first_name,
    last_name,
    gender,
    hire_date,
    age)
ap1()

# def ap():
#     print("\nWelcome Admin!!")
    
#     while True:
#         print("\n---------------------Admin Panel-----------------------")
#         print("\n1.Hire Employee")
#         print("2.Fire Employee")
#         print("3.Change employee data")
#         print("\nInput 0 to quit.")
#         a=input("Enter choice:")
#         if a=='1':
#             ap1()
#         elif a=='2':
#             ap2()
#         elif a=='3':
#             ap3()
#         elif a=='0':
#             print("Quit Admin Panel.")
#             break
#         else:
#             print("Wrong input!(1,2,3)")