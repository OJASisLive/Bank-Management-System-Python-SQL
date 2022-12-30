from employee import deleteaccount
from tools import connection
from panels import clientpanel
conn,cur=connection.cc()
clientpanel.cp(conn,cur)
#alter table current modify column overdraft enum('YES','NO');
#alter table current drop foreign key current_ibfk_1;
#alter table savings drop foreign key savings_ibfk_1;