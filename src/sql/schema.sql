DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS category CASCADE;
DROP TABLE IF EXISTS expense CASCADE;
DROP TABLE IF EXISTS expenses CASCADE;
DROP TABLE IF EXISTS account CASCADE;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL
);

CREATE TABLE account (
    id SERIAL PRIMARY KEY,
    account_id integer REFERENCES users(id),
    last_logged TIMESTAMP,
    create_date DATE
);

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    category TEXT
);

CREATE TABLE expense (
    id SERIAL PRIMARY KEY, 
    name TEXT,
    amount integer,
    category_id integer REFERENCES category(id),
    date DATE,
    added TIMESTAMP,
    comment TEXT
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    expense_id integer REFERENCES expense(id),
    user_owner integer REFERENCES users(id)
);

INSERT INTO category(category) VALUES ('Bills');
INSERT INTO category(category) VALUES ('Entertainment');
INSERT INTO category(category) VALUES ('Hobbies');
INSERT INTO category(category) VALUES ('Groceries');
INSERT INTO category(category) VALUES ('Other');

