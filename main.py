import setup
import check
import accounttype
while True:
    print("1.Continue")
    print("2.Quit")
    a=input("Enter your choice(1,2): ")
    if a == "1":
        if not check.check():
            accounttype.acctype()
            break
        else:
            setup.setup()
    elif a == "2":
        print("Shutting down the program")
        break
    else:
        print("Wrong input.")