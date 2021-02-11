CREATE TABLE corruption(
    id INT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    corrupt_work TEXT,
    PRIMARY KEY(id)
);

CREATE SEQUENCE corruption_sequence_id
START 1
INCREMENT 1
OWNED BY corruption.id;