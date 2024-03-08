-- Anlegen zweier Bücher, Crud

-- books_dict["ISBN1"] = {isbn: "ISBN1", title: "Python"}

INSERT INTO BOOK_RUS (isbn, title) VALUES ('ISBN1', 'Python');
INSERT INTO BOOK_RUS (isbn, title) VALUES ('ISBN2', 'SQL');

-- Suchen: cRud

SELECT isbn, title FROM BOOK_RUS;
SELECT * FROM BOOK_RUS;
SELECT title FROM BOOK_RUS WHERE isbn = 'ISBN1';
SELECT isbn FROM BOOK_RUS WHERE title = 'Python';
SELECT isbn FROM BOOK_RUS WHERE title LIKE 'Python%'; -- Alle Bücher, die mit Python beginnen

-- Aktualisieren: crUd

UPDATE BOOK_RUS SET title = 'Python in Action' WHERE isbn = 'ISBN2';

-- Löschen: cruD

DELETE FROM BOOK_RUS WHERE isbn = 'ISBN1';

