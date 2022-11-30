import mysql.connector
from datetime import date, time

nameDB = 'airline_db'


def populateDB():
    connectToDB()


def connectToDB():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database=nameDB)
    cursor = cnx.cursor()

    createTuples(cursor)

    cnx.commit()
    cursor.close()
    cnx.close()


def createTuples(cursor):
    for i in tuples_tableAirport:
        cursor.execute(commandTuples_tableAirport, tuples_tableAirport[i])
    print('>> tuples in table \'airport\' created')

    for i in tuples_tableAircraft:
        cursor.execute(commandTuples_tableAircraft, tuples_tableAircraft[i])
    print('>> tuples in table \'aircraft\' created')

    for i in tuples_tableCanLand:
        cursor.execute(commandTuples_tableCanLand, tuples_tableCanLand[i])
    print('>> tuples in table \'can_land\' created')

    for i in tuples_tableSeat:
        cursor.execute(commandTuples_tableSeat, tuples_tableSeat[i])
    print('>> tuples in table \'seat\' created')

    for i in tuples_tableFlight:
        cursor.execute(commandTuples_tableFlight, tuples_tableFlight[i])
    print('>> tuples in table \'flight\' created')


commandTuples_tableAirport = (
    'INSERT INTO airport'
    '(airport_code, name, city, country)'
    'VALUES (%s, %s, %s, %s);'
)
tuples_tableAirport = {0: ('ICN', 'Incheon International Airport', 'Incheon', 'Republic of Korea'),
                       1: ('FRA', 'Frankfurt Airport', 'Frankfurt', 'Germany'),
                       2: ('DXB', 'Dubai International Airport', 'Dubai', 'United Arab Emirates'),
                       3: ('GMP', 'Gimpo International Airport', 'Seoul', 'Republic of Korea'),
                       4: ('CJU', 'Jeju International Airport', 'Jeju City', 'Republic of Korea')}

commandTuples_tableAircraft = (
    'INSERT INTO aircraft'
    '(aircraft_registration_code, model, manufacturer)'
    'VALUES (%s, %s, %s);'
)
tuples_tableAircraft = {0: ('D-A78', '747', 'Boing'), 1: ('D-B22', 'A220', 'Airbus')}

commandTuples_tableCanLand = (
    'INSERT INTO can_land'
    '(airport_code, aircraft_registration_code)'
    'VALUES (%s, %s)'
)
tuples_tableCanLand = {0: ('ICN', 'D-A78'), 1: ('ICN', 'D-B22'),
                       2: ('FRA', 'D-A78'), 3: ('FRA', 'D-B22'),
                       4: ('DXB', 'D-A78'), 5: ('DXB', 'D-B22'),
                       6: ('GMP', 'D-B22'), 7: ('CJU', 'D-B22')}

commandTuples_tableSeat = (
    'INSERT INTO seat'
    '(seat_number, aircraft_registration_code, class, extra_price_factor)'
    'VALUES (%s, %s, %s, %s)'
)
tuples_tableSeat = {0: ('A001', 'D-A78', 'first', '3.00'), 1: ('B001', 'D-A78', 'first', '3.00'),
                    2: ('A011', 'D-A78', 'business', '1.50'), 3: ('B011', 'D-A78', 'business', '1.50'),
                    4: ('C011', 'D-A78', 'business', '1.50'), 5: ('D011', 'D-A78', 'business', '1.50'),
                    6: ('A075', 'D-A78', 'economics', '1.00'), 7: ('B075', 'D-A78', 'economics', '1.00'),
                    8: ('C075', 'D-A78', 'economics', '1.00'), 9: ('D075', 'D-A78', 'economics', '1.00'),
                    10: ('A002', 'D-B22', 'business', '1.50'), 11: ('B002', 'D-B22', 'business', '1.50'),
                    12: ('A022', 'D-B22', 'economics', '1.50'), 13: ('B022', 'D-B22', 'economics', '1.50'),
                    14: ('C022', 'D-B22', 'economics', '1.50'), 15: ('D022', 'D-B22', 'economics', '1.50')}

commandTuples_tableFlight = (
    'INSERT INTO flight'
    '(departure_airport_code, arrival_airport_code, aircraft_registration_code,'
    'departure_time, departure_date, arrival_time, arrival_date, base_price)'
    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
)
tuples_tableFlight = {0: ('ICN', 'FRA', 'D-A78', time(6, 5), date(2023, 1, 1), time(19, 5), date(2023, 1, 1), 500),
                      1: ('FRA', 'ICN', 'D-A78', time(7, 5), date(2023, 1, 2), time(19, 5), date(2023, 1, 2), 500),
                      2: ('ICN', 'DXB', 'D-A78', time(5, 0), date(2023, 1, 3), time(11, 30), date(2023, 1, 3), 300),
                      3: ('DXB', 'ICN', 'D-A78', time(12, 30), date(2023, 1, 3), time(19, 0), date(2023, 1, 3), 300),
                      4: ('GMP', 'CJU', 'D-B22', time(8, 0), date(2023, 1, 1), time(9, 0), date(2023, 1, 1), 100),
                      5: ('CJU', 'GMP', 'D-B22', time(11, 45), date(2023, 1, 1), time(12, 45), date(2023, 1, 1), 100)}
