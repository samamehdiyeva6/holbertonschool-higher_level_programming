-- hfjhsgdjm
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
)

INSERT INTO IF EXISTS second_table(id, name, score)
VALUES(1, 'John', 10),
VALUES(1, 'Alex', 3),
VALUES(1, 'Bob', 14),
VALUES(1, 'George', 8)