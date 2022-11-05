import setup
import check
import accounttype
conn=setup.setup()
if not check.check():
    accounttype.acctype()
