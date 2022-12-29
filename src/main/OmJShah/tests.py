from employee import deleteaccount
from tools import connection
from admin import showemployee
from employee import showaccounts
conn,cur=connection.cc()
showaccounts.ep4(cur)
#showemployee.ap4(cur)
#deleteaccount.ep3(conn,cur)
#alter table current modify column overdraft enum('YES','NO');
#alter table current drop foreign key current_ibfk_1;
#alter table savings drop foreign key savings_ibfk_1;