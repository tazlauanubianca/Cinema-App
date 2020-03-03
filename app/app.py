from typing import List, Dict
import mysql.connector
import json
import sys

def get_Planes():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'planes'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM flights')
    results = [[ID, source, destination, hour, \
                    day, duration, seats, reservations, tickets_sold] \
                        for (ID, source, destination, hour, \
                    day, duration, seats, reservations, tickets_sold) in cursor]

    cursor.close()
    connection.close()

    return results

def add_Flight(source, dest, departureDay, departureHour, duration, \
        numberOfSeats, flightID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'planes'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    add_flight = ("INSERT INTO flights (ID, source, destination, hour, day, "
                 "duration, seats, reservations, tickets_sold) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    flight_data = (flightID, source, dest, departureHour, departureDay, duration, numberOfSeats, '0', '0')

    cursor.execute(add_flight, flight_data)
    connection.commit()

    connection.close()
    cursor.close()

def cancel_Flight(flightID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'planes'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    delete_flight = ("DELETE FROM flights where ID = %s")
    flight_data = (flightID, )

    cursor.execute(delete_flight, flight_data)
    connection.commit()

    connection.close()
    cursor.close()


def print_Menu():
    print("Hello to database administration")
    print("Menu: <select number of option>")
    print("1. Add flight")
    print("2. Cancel flight")
    print("3. Print data base")
    print("4. Exit")

if __name__ == '__main__':
    for line in sys.stdin:
        command = line.rstrip()

        if 'menu' == command:
            print_Menu()

        if '1' == command:
            print("Adding flight")
            
            flightID = input("Flight ID: ")
            source = input("Source: ")
            dest = input("Destination: ")
            hour = input("Hour of departure: ")
            day = input("Day of departure: ")
            duration = input("Duration of flight: ")
            numberOfSeats = input("Number of seats available: ")

            add_Flight(source, dest, day, hour, duration, numberOfSeats, flightID)
            print("Flight added!")

        if '2' == command:
            print("Cancel flight")
            flightID = input("Flight ID: ")

            cancel_Flight(flightID)
            print("Flight canceled!")

        if '3' == command:
            print("Planes data base")
            flights = get_Planes()

            for index in range(len(flights)):
                print(flights[index])

        if '4' == command:
            break

