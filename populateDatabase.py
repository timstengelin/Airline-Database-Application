import mysql.connector

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
