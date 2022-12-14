test = {}
test['a'] = (
    'hallo'
        'te\'s\'t'
)

print(test['a'])

select
a = {}
a[0] = 'AA'
a[1] = 'BB'

for i in a:
    print(a[i])

import mysql.connector
from mysql.connector import errorcode
import populateDatabase
nameDB = 'airline_db'


cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='airline_db')
cursor = cnx.cursor()

try:
    cursor.execute('USE airline_db')
except mysql.connector.Error as err:
    # create database
    # ...
    cursor.execute('CREATE DATABASE airline_db')
    # ...

cursor.close()
cnx.close()


##### Code Examples ####

# Code Example 01
cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='airline_db')

# operation with database ...

cnx.close()


# Code Example 02
tables = {}
tables['flight_ticket'] = (
    'CREATE TABLE flight_ticket ('
        'booking_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
        'username varchar(10) NOT NULL,'
        'flight_number int(6) ZEROFILL NOT NULL,'
        'seat_number char(4) NOT NULL,'
        'PRIMARY KEY (booking_number),'
        'FOREIGN KEY (username) REFERENCES customer (username) ON DELETE CASCADE,'
        'FOREIGN KEY (flight_number) REFERENCES flight (flight_number) ON DELETE CASCADE,'
        'FOREIGN KEY (seat_number) REFERENCES seat (seat_number) ON DELETE CASCADE'
    ');'
)
# ...

cursor = cnx.cursor()
# ...
for tableName in tables:
    command = tables[tableName]
    # ...
    cursor.execute(command)
    # ...
cursor.close()


# Code Example 03
commandTuples_tableAircraft = (
    'INSERT INTO aircraft'
    '(aircraft_registration_code, model, manufacturer)'
    'VALUES (%s, %s, %s);'
)
tuples_tableAircraft = {0: ('D-A78', '747', 'Boing'), 1: ('D-B22', 'A220', 'Airbus')}
# ...

cursor = cnx.cursor()
# ...
for i in tuples_tableAircraft:
    cursor.execute(commandTuples_tableAircraft, tuples_tableAircraft[i])
    # ...
cursor.close()




