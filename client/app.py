from typing import List, Dict
from flask import Flask
from tabulate import tabulate
import pandas as pd
import json
import sys
import requests
import mysql.connector

def print_Menu():
    print("Hello Client\n")
    print("Menu: <select number of option>")
    print("1. Show Program")
    print("2. Book Tickets")
    print("3. Buy Tickets")
    print("4. Exit\n")

if __name__ == '__main__':
    url = sys.argv[1]

    for line in sys.stdin:
        command = line.rstrip()

        if 'menu' == command:
            print_Menu()

        if '1' == command:
            print("Cinema program")
            
            day = input("Day (0 - 31): ")
            month = input("Month (1 - 12): ")
            payload = {'day': day, 'month': month}

            session = requests.Session()
            session.trust_env = False
            res = session.get(url + 'getProgram', params=payload)
            route = res.json()

            number_movies = int(route["num_movies"])
            movie_names = []
            movie_times = []
            movie_durations = []
            movie_IDs = []
            
            if number_movies > 0:
                for index in range(number_movies):
                    movie_names.append(route["name_movie" + str(index)])
                    movie_times.append(route["time" + str(index)])
                    movie_durations.append(route["duration" + str(index)])
                    movie_IDs.append(route["ID" + str(index)])

                df = pd.DataFrame({'ID' : movie_IDs,
                                   'Movie' : movie_names,
                                   'Hour' : movie_times,
                                   'Duration' : movie_durations})
                print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

            else:
                print("No movies were found for the given date and month")
            
        if '2' == command:
            print("Book Tickets")

            movie_ID = input("ID Movie: ")
            number_tickets = input("Number of tickets: ")
            payload = {"ID" : movie_ID, "num_reservations" : number_tickets}

            session = requests.Session()
            session.trust_env = False
            res = session.get(url + 'book', params=payload)
            booking = res.json()

            if booking["status"] == "success":
                print("The booking was done! Reservation number: " + str(booking["reservation"]))
            else:
                print(booking["reservation"])

        if '3' == command:
            print("Buy Movie Tickets")

            reservation_number = input("Reservation number: ")
            credit_card = input("Credit card information: ")
            payload = {'reservation_number': reservation_number, "credit_card": credit_card}

            session = requests.Session()
            session.trust_env = False
            res = session.get(url + 'buy', params=payload)
            purchase = res.json()

            print(purchase["status"])

        if '4' == command:
            break
