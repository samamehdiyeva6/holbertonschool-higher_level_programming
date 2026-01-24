-- fedsfsd
CREATE TABLE hbtn_0d_usa.cities(
    id INT NOT NULL AUTO INCREMENT,
    status_id INT NOT NULL,
    name VARCHAR(256),
    PRIMARY KEY(id),
    FOREIGN KEY(status_id) REFERENCES states(id)
)