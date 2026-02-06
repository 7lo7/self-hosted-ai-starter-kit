-- This script generate syntetic data to compile the table and test them --

INSERT INTO behaviour (name, surname, email, O, C, E, A, N)
SELECT 
    (ARRAY['Alice','Bob','Charlie','Diana','Eve'])[FLOOR(RANDOM()*5 +1)::INTEGER],
    (ARRAY['Smith','Johnson','Williams','Brown','Jones'])[FLOOR(RANDOM()*5 +1)::INTEGER],
    'user' || i || '@example.com',
    FLOOR(RANDOM() * 5 + 1)::INTEGER,
    FLOOR(RANDOM() * 5 + 1)::INTEGER,
    FLOOR(RANDOM() * 5 + 1)::INTEGER,
    FLOOR(RANDOM() * 5 + 1)::INTEGER,
    FLOOR(RANDOM() * 5 + 1)::INTEGER
FROM generate_series(1,1000) AS s(i);
