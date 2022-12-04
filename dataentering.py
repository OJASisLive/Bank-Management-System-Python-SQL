from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def primary_key_no(x):
#Employee number and client number
    while True:
        emp_no=input("Enter {} (max 5 int): ".format(x))
        if len(emp_no) <= 5:
            try:
                emp_no=int(emp_no)
                print("Done OK")
            except ValueError:
                print("{} should be an integer!!".format(x))
            else:
                return emp_no
                break
        else:
            print("Maximum length is 5!")

def birthdate(person,minage,maxage):     
#Employee Birth date and client birth date
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
            if age(birth_date)>=minage and age(birth_date)<=maxage:
                return birth_date
                break
            else:
                if age(birth_date)<minage:
                    print("{} must be atleast {} years of age!!".format(person,minage))
                else:
                    print("Maximum age is {} years!!!".format(maxage))
                print("\nwrong input\n")

def name():
#Employee name and client name     
    while True:
        first_name=input("Enter first name (max 15 char): ")
        if len(first_name)<= 15:
            break
        else:
            print("Max 15 characters")

    while True:
        last_name=input("Enter last name (max 15 char): ")
        if len(last_name)<= 15:
            break
        else:
            print("Max 15 characters")
    
    return first_name,last_name

def gender():
#Employee Gender and client gender
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
    return gender

def date2(person,birth_date,hire_or_creation,minage,maxage):
#Employee hire date and account creation date
    while True:
        while True:
            hyear=input("Enter {} year (4 int): ".format(hire_or_creation))
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
            hmonth=input("Enter {} month (2 int) (01 to 12): ".format(hire_or_creation))
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
            hday=input("Enter {} day (2 int) (01 to 31): ".format(hire_or_creation))
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
            if age(hire_date)>maxage:
                print("{} must be below {} years of age!!".format(person,maxage))
            elif age(birth_date)-age(hire_date)>=minage:
                break
            else:
                print("{} must atleast be {} years of age!!".format(person,maxage))
    return hire_date