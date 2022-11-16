import adminpanel
import employeepanel
def acctype():
    while True:
        print("--------------Account Selector Menu--------------")
        print("1.Admin.")
        print("2.Employee.")
        print("3.Client.")
        print("Enter 0 to end process.")
        a=input("\nEnter your account type:")
        
        if a=='1':
            b=input("\nEnter admin password:")
            if b=="admin123":
                adminpanel.ap()
            else:
                print("\nWrong password!\n") 
            
        elif a=='2':
            b=input("\nEnter employee password:")
            if b=="emp123":
                employeepanel.ep()
            else:
                print("\nWrong password!\n")
        
        elif a=='3':
            return 3
        
        elif a=='0':
            print("\nShutting down the program.")
            break
        
        else:
            print("\nWrong input!")