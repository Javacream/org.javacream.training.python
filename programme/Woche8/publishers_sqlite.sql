-- Tabelle: Publisher
CREATE TABLE publisher (
    publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT
);

-- Tabelle: Book
CREATE TABLE book (
    isbn TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    pages INTEGER,
    price REAL,
    publisher_id INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Tabelle: Author
CREATE TABLE author (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL
);

-- Zwischentabelle für m:n Beziehung: Book_Author
CREATE TABLE book_author (
    book_isbn TEXT,
    author_id INTEGER,
    PRIMARY KEY (book_isbn, author_id),
    FOREIGN KEY (book_isbn) REFERENCES book(isbn)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (author_id) REFERENCES author(author_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
