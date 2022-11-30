import mysql.connector
from mysql.connector import errorcode
import populateDatabase

nameDB = 'airline_db'


def initDB():
    connectToDB()


def connectToDB():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root')
    cursor = cnx.cursor()

    try:
        cursor.execute('USE {}'.format(nameDB))
        print('>> database \'{}\' already existing'.format(nameDB))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            createDB(cursor)
            cnx.database = nameDB
            createTables(cursor)
            populateDatabase.populateDB()
        else:
            print(err)
            exit(1)

    cursor.close()
    cnx.close()


def createDB(cursor):
    try:
        cursor.execute('CREATE DATABASE {}'.format(nameDB))
        print('>> database \'{}\' created'.format(nameDB))
    except mysql.connector.Error as err:
        print(err)
        exit(1)


def createTables(cursor):
    for tableName in tables:
        command = tables[tableName]
        try:
            cursor.execute(command)
            print('>> table \'{}\' created'.format(tableName))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('>> table \'{}\' already existing'.format(tableName))
            else:
                print(err)
                exit(1)


tables = {}
tables['customer'] = (
    'CREATE TABLE customer ('
        'username varchar(10) NOT NULL,'
        'first_name varchar(10) NOT NULL,'
        'last_name varchar(10) NOT NULL,'
        'birth_date date NOT NULL,'
        'PRIMARY KEY (username)'
    ');'
)
tables['mobile_number'] = (
    'CREATE TABLE mobile_number ('
        'mobile_number char(13) NOT NULL,'
        'username varchar(10) NOT NULL,'
        'PRIMARY KEY (mobile_number),'
        'FOREIGN KEY (username) REFERENCES customer (username) ON DELETE CASCADE'
    ');'
)
tables['airport'] = (
    'CREATE TABLE airport ('
        'airport_code char(3) NOT NULL,'
        'name varchar(30) NOT NULL,'
        'city varchar(30) NOT NULL,'
        'country varchar(30) NOT NULL,'
        'PRIMARY KEY (airport_code)'
    ');'
)
tables['aircraft'] = (
    'CREATE TABLE aircraft ('
        'aircraft_registration_code char(5) NOT NULL,'
        'model varchar(10) NOT NULL,'
        'manufacturer varchar(10) NOT NULL,'
        'PRIMARY KEY (aircraft_registration_code)'
    ');'
)
tables['can_land'] = (
    'CREATE TABLE can_land ('
        'airport_code char(3) NOT NULL,'
        'aircraft_registration_code char(5) NOT NULL,'
        'PRIMARY KEY (airport_code, aircraft_registration_code),'
        'FOREIGN KEY (airport_code) REFERENCES airport (airport_code) ON DELETE CASCADE,'
        'FOREIGN KEY (aircraft_registration_code) REFERENCES aircraft (aircraft_registration_code) ON DELETE CASCADE'
    ');'
)
tables['seat'] = (
    'CREATE TABLE seat ('
        'seat_number char(4) NOT NULL,'
        'aircraft_registration_code char(5) NOT NULL,'
        'class enum(\'economics\',\'business\',\'first\') NOT NULL,'
        'extra_price_factor numeric(3,2) NOT NULL,'
        'PRIMARY KEY (seat_number, aircraft_registration_code),'
        'FOREIGN KEY (aircraft_registration_code) REFERENCES aircraft (aircraft_registration_code) ON DELETE CASCADE'
    ');'
)
tables['flight'] = (
    'CREATE TABLE flight ('
        'flight_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
        'departure_airport_code char(3) NOT NULL,'
        'arrival_airport_code char(3) NOT NULL,'
        'aircraft_registration_code char(5) NOT NULL,'
        'departure_time time NOT NULL,'
        'departure_date date NOT NULL,'
        'arrival_time time NOT NULL,'
        'arrival_date date NOT NULL,'
        'base_price smallint NOT NULL,'
        'PRIMARY KEY (flight_number),'
        'FOREIGN KEY (departure_airport_code) REFERENCES airport (airport_code) ON DELETE CASCADE,'
        'FOREIGN KEY (arrival_airport_code) REFERENCES airport (airport_code) ON DELETE CASCADE,'
        'FOREIGN KEY (aircraft_registration_code) REFERENCES aircraft (aircraft_registration_code) ON DELETE CASCADE'
    ');'
)
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
tables['hold_luggage'] = (
    'CREATE TABLE hold_luggage ('
        'luggage_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
        'booking_number int(6) ZEROFILL NOT NULL,'
        'weight smallint NOT NULL,'
        'PRIMARY KEY (luggage_number),'
        'FOREIGN KEY (booking_number) REFERENCES flight_ticket (booking_number) ON DELETE CASCADE'
    ');'
)
tables['animal_luggage'] = (
    'CREATE TABLE animal_luggage ('
        'luggage_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
        'booking_number int(6) ZEROFILL NOT NULL,'
        'animal_species varchar(10) NOT NULL,'
        'PRIMARY KEY (luggage_number),'
        'FOREIGN KEY (booking_number) REFERENCES flight_ticket (booking_number) ON DELETE CASCADE'
    ');'
)