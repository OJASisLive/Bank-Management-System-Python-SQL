def check():
    with open("firsttime.txt","r") as a:
        if a.read()=="True":
            return True
        else:
            return False