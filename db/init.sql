CREATE DATABASE IF NOT EXISTS cinema;

use cinema;

CREATE TABLE movies (
  ID VARCHAR(20),
  name_movie VARCHAR(150),
  time VARCHAR(40),
  day INT,
  month INT,
  duration INT,
  seats INT,
  reservations INT,
  tickets_sold INT
);

INSERT INTO movies
  (ID, name_movie, time, day, month, duration, seats, reservations, tickets_sold)
VALUES
  (0, 'How To Train Your Dragon', '13:00', 10, 02, 124, 100, 13, 23),
  (1, 'Inception', '22:30', 2, 03, 156, 200, 0, 0);
