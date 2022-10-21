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
    "  `age` int(2) NOT NULL"
    "  PRIMARY KEY (`emp_no`)"
    ") ")

TABLES['client'] = (
    "CREATE TABLE `clients` ("
    "  `acc_no` int(5) NOT NULL AUTO_INCREMENT,"
    "  `acc_type` enum('S','C') NOT NULL"
    "  `first_name` varchar(15) NOT NULL,"
    "  `last_name` varchar(15) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `birth_date` date NOT NULL,"
    "  `acc_creation_date` date NOT NULL,"
    "  PRIMARY KEY (`acc_no`)"
)

#https://education.github.com/git-cheat-sheet-education.pdf
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
    