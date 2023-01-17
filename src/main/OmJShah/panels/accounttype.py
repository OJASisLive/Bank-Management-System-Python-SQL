from panels import adminpanel
from panels import employeepanel
from panels import clientpanel
def acctype(query,cur):
    while True:
        print("--------------Account Selector Menu--------------")
        print("1.Admin.")
        print("2.Employee.")
        print("3.Client.")
        print("Enter ~ to end process.")
        a=input("\nEnter your account type:")
        
        if a=='1':
            b=input("\nEnter admin password:")
            if b=="admin123":
                adminpanel.ap(query,cur)
            else:
                print("\nWrong password!\n") 
            
        elif a=='2':
            b=input("\nEnter employee password:")
            if b=="emp123":
                employeepanel.ep(query,cur)
            else:
                print("\nWrong password!\n")
        
        elif a=='3':
            clientpanel.cp(query,cur)
        
        elif a=='~':
            print("\nShutting down the program.")
            break
        
        else:
            print("\nWrong input!")