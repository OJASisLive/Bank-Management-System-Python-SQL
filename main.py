import setup
import check
import accounttype
while True:
    if not check.check():
        accounttype.acctype()
        break
    else:
        setup.setup()
