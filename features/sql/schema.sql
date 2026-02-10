-- first define the database --
CREATE extension IF NOT EXISTS vector;
CREATE TABLE behaviour (
    userid SERIAL PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(50),
    email TEXT UNIQUE,
    O INTEGER DEFAULT 0,
    C INTEGER DEFAULT 0,
    E INTEGER DEFAULT 0,
    A INTEGER DEFAULT 0,
    N INTEGER DEFAULT 0,
    embedding vector(768)
);
