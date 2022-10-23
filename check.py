def check():
    with open("firsttime.txt","r") as a:
        if a.read().strip()=="True":
            return True
        else:
            return False