CREATE EXTENSION 'uuid-ossp';

CREATE TABLE users(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    PRIMARY KEY(ID)
)