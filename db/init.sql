CREATE DATABASE IF NOT EXISTS cinema;

use cinema;

CREATE TABLE movies (
  ID VARCHAR(20),
  name_movie VARCHAR(150),
  time VARCHAR(40),
  room VARCHAR(40),
  day INT,
  month INT,
  duration INT,
  seats INT,
  reservations INT,
  tickets_sold INT
);

CREATE TABLE reservations (
	ID varchar(20),
	ID_movie varchar(20),
	num_reservations INT
);

INSERT INTO movies
  (ID, name_movie, time, room, day, month, duration, seats, reservations, tickets_sold)
VALUES
  (0, 'How To Train Your Dragon', '13:00', '9', 10, 2, 124, 100, 13, 23),
  (1, 'Inception', '22:30', '10', 2, 3, 156, 200, 0, 0),
  (2, 'Escape Room', '20:12', '3', 2, 3, 167, 100, 0, 0),
  (3, 'A Dog\'s Purpose', '12:34', '1', 2, 3, 127, 67, 0, 0),
  (4, 'A Dog\'s Purpose', '13:34', '1', 2, 3, 127, 67, 0, 0),
  (5, 'A Dog\'s Purpose', '14:34', '1', 2, 3, 127, 67, 0, 0),
  (6, 'A Dog\'s Purpose', '15:34', '1', 2, 3, 127, 67, 0, 0),
  (7, 'A Dog\'s Purpose', '16:34', '1', 2, 3, 127, 67, 0, 0),
  (8, 'A Dog\'s Purpose', '17:34', '1', 2, 3, 127, 67, 0, 0),
  (9, 'A Dog\'s Purpose', '18:34', '1', 2, 3, 127, 67, 0, 0),
  (10, 'A Dog\'s Purpose', '19:34', '1', 2, 3, 127, 67, 0, 0),
  (11, 'A Dog\'s Purpose', '20:34', '1', 2, 3, 127, 67, 0, 0),
  (12, 'A Dog\'s Purpose', '21:34', '1', 2, 3, 127, 67, 0, 0),
  (13, 'A Dog\'s Purpose', '22:34', '1', 2, 3, 127, 67, 0, 0),
  (14, 'A Dog\'s Purpose', '23:34', '1', 2, 3, 127, 67, 0, 0),
  (15, 'A Dog\'s Purpose', '03:34', '1', 2, 3, 127, 67, 0, 0);
