DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS expenses CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL
);

CREATE TABLE expenses (id SERIAL PRIMARY KEY, name TEXT, amount integer,
    category TEXT,
    date DATE,
    added TIMESTAMP,
    comment TEXT,
    user_owner integer REFERENCES users(id)
);
