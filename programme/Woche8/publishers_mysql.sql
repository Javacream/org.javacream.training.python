-- Tabelle: Publisher
CREATE TABLE publisher (
    publisher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255)
);

-- Tabelle: Book
CREATE TABLE book (
    isbn VARCHAR(20) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    pages INT,
    price DECIMAL(10, 2),
    publisher_id INT,
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Tabelle: Author
CREATE TABLE author (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL
);

-- Zwischentabelle für m:n Beziehung: Book_Author
CREATE TABLE book_author (
    book_isbn VARCHAR(20),
    author_id INT,
    PRIMARY KEY (book_isbn, author_id),
    FOREIGN KEY (book_isbn) REFERENCES book(isbn)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (author_id) REFERENCES author(author_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
