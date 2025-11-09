CREATE TABLE users (
    user_id PRIMARY KEY SERIAL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT  CURRENT_TIMESTAMP,
    university VARCHAR(100),
    graduation_year INTEGER
);

CREATE TABLE rides(
    ride_id SERIAL PRIMARY KEY,
    driver_id INTEGER REFERENCES users(user_id),
    origin VARCHAR(255) NOT NULL,
    destination VARCHAR(200) NOT NULL,
    departure_time TIMESTAMP NOT NULL,
    seats_available INTEGER NOT NULL,
    price_per_seat DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'available',
    created_at TIMESTAMP DEFAULT  CURRENT_TIMESTAMP
);

CREATE TABLE bookings(
    booking_id PRIMARY KEY SERIAL,
    ride_id INTEGER REFERENCES rides(ride_id),
    passenger_id INTEGER REFERENCES users(user_id),
    seast_booked INTEGER NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    boking_time TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'confirmed',
    rating INTEGER CHECK (rating BETWEEN 1 AND 5)
);


CREATE TABLE payments(
    payment_id PRIMARY KEY SERIAL,
    booking_id INTEGER REFERENCES bookings(booking_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50),
    payment_status VARCHAR(20), -- pending, completed, failed, refunded
    payment_time TIMESTAMP,
    stripe_charge_id VARCHAR(200)
);

CREATE TABLE reviews(
    review_id PRIMARY KEY SERIAL,
    booking_id INTEGER REFERENCES bookings(booking_id),
    reviewer_id INTEGER REFERENCES users(user_id),
    reviewwee_id INTEGER REFERENCES users(user_id),
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP default CURRENT_TIMESTAMP
);

--- PATTERN MATCHING WITH LIKE
SELECT
    user_id, name, email
FROM
    users
WHERE
 email LIKE '%@williams.edu' AND name LIKE '____';


--- MULTIPLE SORT CRITERIA
SELECT name, university, graduation_year
FROM users
ORDER BY name ASC, graduation_year DESC, university ASC
LIMIT 20;


--- ORDER BY EXPRESSION
SELECT name, email, phone
FROM users
WHERE EXTRACT(YEAR FROM created_at) < 2025
ORDER BY EXTRACT (YEAR FROM created_at) DESC, name ASC
LIMIT 10 OFFSET 10;

SELECT ride_id, origin, destination, price_per_seat 
FROM rides
ORDER BY price_per_seat DESC
LIMIT 5;


---AGGREGATE FUNCTIONS
SELCET COUNT(*) AS total_users
FROM users;

SELECT COUNT(phone) as users_with_phone
FROM users;

SELECT COUNT(DISTINCT university) as universities
FROM users;

SELECT AVG(price_per_seat) AS avg_price
FROM rides;


SELECT SUM(total_amount) AS total_revenues
FROM bookings;

SELECT 
    user_id,
    SUM(total_amount) as amount_spent
FROM bookings

--MAU by at least one ride
SELECT 
    DATE_TRUNC('month', booking_time),
    COUNT(DISTINCT passenger_id) AS monthly_active_users
FROM bookings
WHERE
    booking_time >= CURRENT_DATE - INTERVAL '12 months'

GROUP BY DATE_TRUNC('month', booking_time)
ORDER BY month DESC;



-- JOINS
SELECT
    r.ride_id,
    r.origin,
    r.destination,
    r.price_per_seat,
    r.seats_available,
    u.name AS driver_name,
    u.email AS driver_email,
    u.phone
FROM rides r
INNER JOIN users u on r.driver_id = u.user_id
WHERE r.status = 'available'
ORDER BY
    r.departure_time DESC
    r.seats_available DESC
LIMIT 20;


SELECT
    b.booking_id,
    b.seast_booked,
    b.total_amount,
    u.name AS passenger_name,
    u.phone AS passenger_phone
    r.origin,
    r.destnation,
    r.departure_time
FROM bookings b
JOIN users u on b.passenger_id = u.user_id
JOIN rides r on b.ride_id = r.ride_id
WHERE b.status = 'confirmed'
ORDER BY r.departure_time


SELECT 
    u.user_id,
    u.name,
    u.email,
    COUNT(b.booking_id) AS total_bookings,
    COALESCE(SUM(b.total_amount), 0) AS amount_spent
FROM users u 
LEFT JOIN bookings b on u.user_id = b.passenger_id
    


