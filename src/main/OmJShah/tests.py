from employee import deleteaccount
from tools import connection
from admin import showemployee
from employee import showaccounts
conn,cur=connection.cc()
showaccounts.ep4(cur)
#showemployee.ap4(cur)
#deleteaccount.ep3(conn,cur)