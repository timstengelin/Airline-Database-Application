import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='airlinedatabase'
)

cursor = db.cursor()

# createDb()

cursor.execute('show databases')
for i in cursor:
    print(i)


def createDB():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
    )

    cursor = cnx.cursor()

    cursor.execute('create database airlineDatabase')


def createConnectionToDB():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='airlinedatabase')
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()


def closeConnectionToDB(cnx):
    cnx.close()

def createCursor(cnx):
    cursor = cnx.cursor()

def createTables():
    tables = {}
    tables['customer'] = (
        'CREATE TABLE customer ('
            'username varchar(10) NOT NULL,'
            'first_name varchar(10),'
            'last_name varchar(10),'
            'birth_date date,'
            'PRIMARY KEY (username)'
        ');'
    )
    tables['mobile_number'] = (
        'CREATE TABLE mobile_number ('
            'mobile_number char(13) NOT NULL,'
            'username varchar(10),'
            'PRIMARY KEY (mobile_number),'
            'FOREIGN KEY (username) REFERENCES customer'
        ');'
    )
    tables['flight_ticket'] = (
        'CRATE TABLE flight_ticket ('
            'booking_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
            'username varchar(10),'
            'flight_number int(6) ZEROFILL,'
            'seat_number char(5),'
            'PRIMARY KEY (booking_number),'
            'FOREIGN KEY (flight_number) REFERENCES flight,'
            'FOREIGN KEY (seat_number) REFERENCES seat'
        ');'
    )
    tables['seat'] = (
        'CREATE TABLE seat ('
            'seat_number char(5) NOT NULL,'
            'aircraft_registration_code char(5) NOT NULL,'
            'class enum(\'economic\',\'business\',\'first\'),'
            'extra_price_factor numeric(3,2),'
            'PRIMARY KEY (seat_number, aircraft_registration_code),'
            'FOREIGN KEY (aircraft_registration_code) REFERENCES aircraft'
        ');'
    )
    tables['hold_luggage'] = (
        'CREATE TABLE hold_luggage ('
            'luggage_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
            'booking_number int(6) ZEROFILL,'
            'weight smallint,'
            'PRIMARY KEY (luggage_number),'
            'FOREIGN KEY (booking_number) REFERENCES flight_ticket'
        ');'
    )
    tables['animal_luggage'] = (
        'CREATE TABLE animal_luggage ('
            'luggage_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
            'booking_number int(6) ZEROFILL,'
            'animal_species varchar(10),'
            'PRIMARY KEY (luggage_number),'
            'FOREIGN KEY (booking_number) REFERENCES flight_ticket'
        ');'
    )
    tables['flight'] = (
        'CREATE TABLE flight ('
            'flight_number int(6) ZEROFILL NOT NULL AUTO_INCREMENT,'
            'departure_airport_registration_code char(3),'
            'arrival_airport_registration_code char(3),'
            'aircraft_registration_code char(5),'
            'departure_time time,'
            'departure_date date,'
            'arrival_time time,'
            'arrival_date date,'
            'base_price smallint,'
            'PRIMARY KEY (flight_number),'
            'FOREIGN KEY (departure_airport_registration_code) REFERENCES airport,'
            'FOREIGN KEY (arrival_airport_registration_code) REFERENCES airport,'
            'FOREIGN KEY (aircraft_registration_code) REFERENCES aircraft'
        ');'
    )
    tables['aircraft'] = (
        'CREATE TABLE aircraft ('
            'aircraft_registration_code char(5) NOT NULL,'
            'model varchar(10),'
            'manufacturer varchar(10),'
            'PRIMARY KEY (aircraft_registration_code)'
        ');'
    )
    tables['airport'] = (
        'CREATE TABLE airport ('
            'airport_code char(3) NOT NULL,'
            'name varchar(10),'
            'city varchar(10),'
            'country varchar(10),'
            'PRIMARY KEY (airport_code)'
        ');'
    )
    tables['can_land'] = (
        'CREATE TABLE can_land ('
            'airport_code char(3) NOT NULL,'
            'aircraft_registration_code char(5) NOT NULL,'
            'PRIMARY KEY (airport_code, aircraft_registration_code),'
            'FOREIGN KEY (airport_code) REFERENCES airport,'
            'FOREIGN KEY (aircraft_registration_code) REFERENCES aircraft'
        ');'
    )
