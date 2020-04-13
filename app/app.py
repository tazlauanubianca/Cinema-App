from typing import List, Dict
import mysql.connector
import json
import sys

def get_Movies():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM movies')
    results = [[ID, name_movie, time, day, month, \
                duration, seats, reservations, tickets_sold] \
                for (ID, name_movie, time, day, month, \
                duration, seats, reservations, tickets_sold) in cursor]

    cursor.close()
    connection.close()

    return results

def add_Movie(name, time, day, month, duration, seats, ID, room):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    add_movie = ("INSERT INTO movies (ID, name_movie, time, room, day, "
                 "month, duration, seats, reservations, tickets_sold) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    movie_data = (ID, name, time, room, day, month, duration, seats, '0', '0')

    cursor.execute(add_movie, movie_data)
    connection.commit()
    connection.close()
    cursor.close()

def cancel_Movie(ID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    delete_movie = ("DELETE FROM movies where ID = %s")
    movie_data = (ID, )

    cursor.execute(delete_movie, movie_data)
    connection.commit()

    connection.close()
    cursor.close()


def print_Menu():
    print("Hello to database administration")
    print("Menu: <select number of option>")
    print("1. Add movie")
    print("2. Cancel movie")
    print("3. Print data base")
    print("4. Exit")

if __name__ == '__main__':
    for line in sys.stdin:
        command = line.rstrip()

        if 'menu' == command:
            print_Menu()

        if '1' == command:
            print("Adding movie")
            
            ID = input("Movie ID: ")
            name = input("Movie Name: ")
            time = input("Time of display: ")
            day = input("Day of the month: ")
            month = input("Month: ")
            room = input("Room: ")
            duration = input("Duration of the movie: ")
            seats = input("Number of seats available: ")

            add_Movie(name, time, day, month, duration, seats, ID, room)
            print("Movie added!")

        if '2' == command:
            print("Cancel movie")
            ID = input("Movie ID: ")

            cancel_Movie(ID)
            print("Movie canceled!")

        if '3' == command:
            print("Cinema data base")
            movies = get_Movies()

            for index in range(len(movies)):
                print(movies[index])

        if '4' == command:
            break

