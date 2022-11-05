import setup
from check import check
import accounttype
conn=setup.setup()
if not check:
    accounttype.acctype()