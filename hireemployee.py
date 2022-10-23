from datetime import date
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def ap1():
    print("-------------Hire Employee Process-------------")

#Employee number
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
#Employee Birth date
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
        except ValueError:
            import traceback
            traceback.print_exc()
        else:
            if age(birth_date)>=20:
                break
            else:
                print("Employee must be atleast 20 years of age!!")
#Employee name          
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
#Employee Gender
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
#Employee hire date
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
        except ValueError:
            import traceback
            traceback.print_exc()
        else:
            if age(birth_date)-age(hire_date)>=20:
                break
            else:
                print("Employee must atleast be 20 years of age!!")


    print("=========== Final Data ===========")
    x=(emp_no,
    birth_date,
    first_name,
    last_name,
    gender,
    hire_date)
    print(x)
    return x