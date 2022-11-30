import mysql.connector
from datetime import date, time

nameDB = 'airlinedatabase'


def populateDB():
    connectToDB()


def connectToDB():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database=nameDB)
    cursor = cnx.cursor()

    # TODO

    cursor.close()
    cnx.close()


commandTuples_tableAirport = (
    'INSERT INTO airport'
    'VALUES (%s, %s, %s, %s);'
)
tuples_tableAirport = {}
tuples_tableAirport[0] = ('ICN', 'Incheon International Airport', 'Incheon', 'Republic of Korea')
tuples_tableAirport[1] = ('FRA', 'Frankfurt Airport', 'Frankfurt', 'Germany')
tuples_tableAirport[2] = ('DXB', 'Dubai International Airport', 'Dubai', 'United Arab Emirates')
tuples_tableAirport[3] = ('GMP', 'Gimpo International Airport', 'Seoul', 'Republic of Korea')
tuples_tableAirport[4] = ('CJU', 'Jeju International Airport', 'Jeju City', 'Republic of Korea')

commandTuples_tableAircraft = (
    'INSERT INTO aircraft'
    'VALUES (%s, %s, %s);'
)
tuples_tableAircraft = {}
tuples_tableAircraft[0] = ('D-A78', '747', 'Boing')
tuples_tableAircraft[1] = ('D-B22', 'A220', 'Airbus')

commandTuples_tableCanLand = (
    'INSERT INTO can_land'
    'VALUES (%s, %s)'
)
tuples_canLand = {}
tuples_canLand[0] = ('ICN', 'D-A78')
tuples_canLand[1] = ('ICN', 'D-B22')
tuples_canLand[2] = ('FRA', 'D-A78')
tuples_canLand[3] = ('FRA', 'D-B22')
tuples_canLand[4] = ('DXB', 'D-A78')
tuples_canLand[5] = ('DXB', 'D-B22')
tuples_canLand[6] = ('GMP', 'D-B22')
tuples_canLand[7] = ('CJU', 'D-B22')

commandTuples_tableSeat = (
    'INSERT INTO seat'
    'VALUES (%s, %s, %s, %s)'
)
tuples_seat = {}
tuples_seat[0] = ('A001', 'D-A78', 'first', '3.00')
tuples_seat[1] = ('B001', 'D-A78', 'first', '3.00')
tuples_seat[2] = ('A011', 'D-A78', 'business', '1.50')
tuples_seat[3] = ('B011', 'D-A78', 'business', '1.50')
tuples_seat[4] = ('C011', 'D-A78', 'business', '1.50')
tuples_seat[5] = ('D011', 'D-A78', 'business', '1.50')
tuples_seat[6] = ('A075', 'D-A78', 'economics', '1.00')
tuples_seat[7] = ('B075', 'D-A78', 'economics', '1.00')
tuples_seat[8] = ('C075', 'D-A78', 'economics', '1.00')
tuples_seat[9] = ('D075', 'D-A78', 'economics', '1.00')
tuples_seat[10] = ('A002', 'D-B22', 'business', '1.50')
tuples_seat[11] = ('B002', 'D-B22', 'business', '1.50')
tuples_seat[12] = ('A022', 'D-B22', 'economics', '1.50')
tuples_seat[13] = ('B022', 'D-B22', 'economics', '1.50')
tuples_seat[14] = ('C022', 'D-B22', 'economics', '1.50')
tuples_seat[15] = ('D022', 'D-B22', 'economics', '1.50')

commandTuples_tableFlight = (
    'INSERT INTO flight'
    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
)
tuples_flight = {}
tuples_flight[0] = (0, 'ICN', 'FRA', 'D-A78', time(6, 5), date(2023, 1, 1), time(19, 5), date(2023, 1, 1), 500)
tuples_flight[1] = (0, 'FRA', 'ICN', 'D-A78', time(7, 5), date(2023, 1, 2), time(19, 5), date(2023, 1, 2), 500)
tuples_flight[2] = (0, 'ICN', 'DXB', 'D-A78', time(5, 0), date(2023, 1, 3), time(11, 30), date(2023, 1, 3), 300)
tuples_flight[3] = (0, 'DXB', 'ICN', 'D-A78', time(12, 30), date(2023, 1, 3), time(19, 0), date(2023, 1, 3), 300)
tuples_flight[4] = (0, 'GMP', 'CJU', 'D-B22', time(8, 0), date(2023, 1, 1), time(9, 0), date(2023, 1, 1), 100)
tuples_flight[5] = (0, 'CJU', 'GMP', 'D-B22', time(11, 45), date(2023, 1, 1), time(12, 45), date(2023, 1, 1), 100)
