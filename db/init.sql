CREATE DATABASE IF NOT EXISTS planes;

use planes;

CREATE TABLE flights (
  ID VARCHAR(20),
  source VARCHAR(40),
  destination VARCHAR(40),
  hour INT,
  day INT,
  duration INT,
  seats INT,
  reservations INT,
  tickets_sold INT
);

INSERT INTO flights
  (ID, source, destination, hour, day, duration, seats, reservations, tickets_sold)
VALUES
  (0, 'London', 'Madrid', 10, 205, 5, 250, 0, 0),
  (1, 'Bucharest', 'Munich', 2, 156, 2, 200, 0, 0);
