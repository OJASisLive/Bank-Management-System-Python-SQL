import setup
import mysql.connector
from mysql.connector import errorcode
conn=setup.setup()
cursor=conn.cursor()

DB_NAME = setup.sqldb()

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(5) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(15) NOT NULL,"
    "  `last_name` varchar(15) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  `age` int(2) NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ")

TABLES['clients'] = (
    "CREATE TABLE `clients` ("
    "  `acc_no` int(5) NOT NULL AUTO_INCREMENT,"
    "  `acc_type` enum('S','C') NOT NULL,"
    "  `first_name` varchar(15) NOT NULL,"
    "  `last_name` varchar(15) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `birth_date` date NOT NULL,"
    "  `acc_creation_date` date NOT NULL,"
    "  `mobile_no int(10) NOT NULL`,"
    "  `email_id varchar(25) NOT NULL`,"
    "  PRIMARY KEY (`acc_no`)"
    ") "
)

TABLES['savings'] = (
    "CREATE TABLE `savings` ("
    "  `acc_no` int(5) NOT NULL,"
    "  `balance` int NOT NULL,"
    "  `loan` enum('YES','NO') NOT NULL,"
    "  PRIMARY KEY (`acc_no`),"
    "  FOREIGN KEY(`acc_no`) REFERENCES clients(acc_no)"
    ") "
)

TABLES['current'] = (
    "CREATE TABLE `current` ("
    "  `acc_no` int(5) NOT NULL,"
    "  `balance` int NOT NULL,"
    "  `overdraft` int NOT NULL,"
    "  PRIMARY KEY (`acc_no`),"
    "  FOREIGN KEY(`acc_no`) REFERENCES clients(acc_no)"
    ") "
)

TABLES['loan'] = (
    "CREATE TABLE `loan` ("
    "  `acc_no` int(5) NOT NULL,"
    "  `loan_type` enum('PL','HL','EL','TL','BL') NOT NULL,"
    "  `loan_amt` int NOT NULL,"
    "  `time_period_months` int NOT NULL,"
    "  `iterest_perc_per_annum` int(1) NOT NULL,"
    "  `amt-per-month` int NOT NULL,"
    "  `remaining_amt` int NOT NULL,"
    "  PRIMARY KEY (`acc_no`),"
    "  FOREIGN KEY(`acc_no`) REFERENCES clients(acc_no)"
    ") "
)

TABLES['overdraft']=(
    "CREATE TABLE `overdraft` ("
    "  `acc_no` int(5) NOT NULL,"
    "  `overdraft_amt` int NOT NULL,"
    "  `od_with_interest_remaining int NOT NULL,"
    "  PRIMARY KEY (`acc_no`),"
    "  FOREIGN KEY(`acc_no`) REFERENCES clients(acc_no)"
    ") "
)
def tables():
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
#Credits
#https://education.github.com/git-cheat-sheet-education.pdf
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
