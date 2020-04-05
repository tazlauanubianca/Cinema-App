from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json
import random
import string

app = Flask(__name__)

class Movie:
    def __init__(self, ID, name_movie, time, room,\
                day, month, duration, seats,\
                reservations, tickets_sold):
        self.ID = ID
        self.name_movie = name_movie
        self.time = time
        self.room = room
        self.day = day
        self.month = month
        self.duration = duration
        self.seats = seats
        self.reservations = reservations
        self.tickets_sold = tickets_sold

class Reservation:
    def __init__(self, ID, ID_movie, num_reservations):
        self.ID = ID
        self.ID_movie = ID_movie
        self.num_reservations = num_reservations

def random_reservationID(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def get_reservation(ID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    get_reservation = ("SELECT * FROM reservations WHERE ID = %s")
    reservation_data = (ID, )

    cursor.execute(get_reservation, reservation_data)
    reservations = [Reservation(ID, ID_movie, num_reservations) \
                for (ID, ID_movie, num_reservations) in cursor]

    connection.close()
    cursor.close()
    
    if len(reservations) != 1:
        cursor.close()
        connection.close()

        return None

    return reservations[0]

def get_database():
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

    movies = {}
    for (ID, name_movie, time, room, \
        day, month, duration, seats, \
        reservations, tickets_sold) in cursor:
        movie = Movie(ID, name_movie, time, room, \
                int(day), int(month), int(duration), \
                int(seats), int(reservations), \
                int(tickets_sold))
        movies[movie.ID] = movie

    cursor.close()
    connection.close()

    return movies

def reserve_ticket(movie_ID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    get_movie = ("SELECT * FROM movies WHERE ID = %s")
    movie_data = (movie_ID, )

    cursor.execute(get_movie, movie_data)
    movies = [Movie(ID, name_movie, time, room,  \
                    day, month, duration, seats, \
                    reservations, tickets_sold)  \
                for (ID, name_movie, time, room, \
                    day, month, duration, seats, \
                    reservations, tickets_sold) in cursor]

    if len(movies) != 1:
        cursor.close()
        connection.close()

        return len(movies)

    if (int(movies[0].reservations) + 1) <= int(movies[0].seats):
        update_movie = ("UPDATE movies SET reservations = %s WHERE ID = %s")
        movie_data = (int(movies[0].reservations) + 1, movie_ID)
        cursor.execute(update_movie, movie_data)
        connection.commit()

        connection.close()
        cursor.close()

        return 1

    return -1

def buy_ticket(movie_ID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    get_movie = ("SELECT * FROM movies WHERE ID = %s")
    movie_data = (movie_ID, )

    cursor.execute(get_movie, movie_data)
    movies = [Movie(ID, name_movie, time, room,  \
                    day, month, duration, seats, \
                    reservations, tickets_sold)  \
                for (ID, name_movie, time, room, \
                    day, month, duration, seats, \
                    reservations, tickets_sold) in cursor]

    if len(movies) != 1:
        cursor.close()
        connection.close()

        return len(movies)

    if (int(movies[0].reservations) + 1) <= int(movies[0].seats):
        update_movie = ("UPDATE movies SET reservations = %s WHERE ID = %s")
        movie_data = (int(movies[0].reservations) - 1, movie_ID)
        cursor.execute(update_movie, movie_data)
        connection.commit()

        update_movie = ("UPDATE movies SET tickets_sold = %s WHERE ID = %s")
        movie_data = (int(movies[0].tickets_sold) + 1, movie_ID)
        cursor.execute(update_movie, movie_data)
        connection.commit()

        connection.close()
        cursor.close()

        return 1

    return -1

def cancel_reservation(ID):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    delete_reservation = ("DELETE FROM reservations where ID = %s")
    reservation_data = (ID, )

    cursor.execute(delete_reservation, reservation_data)
    connection.commit()
    connection.close()
    cursor.close()

def add_reservation(ID, ID_movie, num_reservations):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cinema'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    add_reservation = ("INSERT INTO reservations (ID, ID_movie, num_reservations)"
                        "VALUES (%s, %s, %s)")
    reservation_data = (ID, ID_movie, num_reservations)

    cursor.execute(add_reservation, reservation_data)
    connection.commit()
    connection.close()
    cursor.close()

@app.route('/getProgram', methods=['GET'])
def get_cinema_program():
    day = request.args.get('day')
    month = request.args.get('month')
    filtered_movies = []
    movies = get_database()

    for movie in movies.values():
        if movie.day == int(day) and movie.month == int(month):
            filtered_movies.append(movie)

    num_movies = len(filtered_movies)
    response = {"num_movies": num_movies}

    for index in range(num_movies):
        response["name_movie" + str(index)] = filtered_movies[index].name_movie
        response["time" + str(index)] = filtered_movies[index].time
        response["duration" + str(index)] = str(filtered_movies[index].duration)
        response["ID" + str(index)] = filtered_movies[index].ID
    
    return response

@app.route('/book', methods=['GET'])
def book():
    num_reservations = int(request.args.get("num_reservations"))
    movie_ID = int(request.args.get("ID"))
    reservation_ID = random_reservationID()

    add_reservation(reservation_ID, movie_ID, num_reservations)
    reservation = reserve_ticket(movie_ID)
    if reservation != 1:
        return {"status" : "fail", "reservation" : "Could not book ticket for movie: " + str(movie_ID)}
 
    return {"status" : "success", "reservation" : reservation_ID}

@app.route('/buy', methods=['GET'])
def buy():
    reservation_ID = request.args.get("reservation_number")
    credit_card = request.args.get("credit_card")
    if credit_card is "":
        return {"status" : "No credit card information provided"}

    reservation = get_reservation(reservation_ID)
    if reservation is not None:
        response = ""

        cancel_reservation(reservation.ID)
        purchase = buy_ticket(reservation.ID_movie)
        if purchase != 1:
            return {"status" : "Could not buy ticket for flight: " + reservation.ID_movie}
        else:
            response = response + " " + reservation.ID_movie

        return {"status" : "The tickets were bought for the movie: " + response}
    else:
        return {"status" : "Reservation number doesn't exist"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
