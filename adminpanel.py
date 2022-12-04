import hireemployee

def ap():
    print("\nWelcome Admin!!")
    
    while True:
        print("\n---------------------Admin Panel-----------------------")
        print("\n1.Hire Employee")
        print("2.Fire Employee")
        print("3.Change employee data")
        print("4.Show employee table")
        print("\nInput 0 to quit.")
        a=input("Enter choice:")
        if a=='1':
            hireemployee.ap1()
        elif a=='2':
            hireemployee.ap2()
        elif a=='3':
            hireemployee.ap3()
        elif a=='4':
            hireemployee.ap4()
        elif a=='0':
            print("Quit Admin Panel.")
            break
        else:
            print("Wrong input!(1,2,3)")

ap()