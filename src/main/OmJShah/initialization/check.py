def check():
    try:
        with open("firsttime.txt","r") as a:
            if a.read().strip()=="True":
                return True
            else:
                return False
    except FileNotFoundError:
        with open("firsttime.txt","w") as a:
            a.write("True")
            return True