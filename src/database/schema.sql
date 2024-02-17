-- database: secretos.db
CREATE TABLE secrets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member VARCHAR(100),
    secret VARCHAR(10000),
    server VARCHAR(10000)
);