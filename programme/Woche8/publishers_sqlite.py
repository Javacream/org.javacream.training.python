import sqlite3
import random

def prepare(conn):
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Tabellen erstellen
    cursor.executescript("""
    CREATE TABLE publisher (
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT
    );

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

    CREATE TABLE author (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL
    );

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
    """)

    # 3 Publisher einfügen
    publishers = [
        ("Springer Verlag", "Heidelberg, Germany"),
        ("O'Reilly Media", "Sebastopol, USA"),
        ("Pearson Education", "London, UK")
    ]
    cursor.executemany("INSERT INTO publisher (name, address) VALUES (?, ?)", publishers)

    # 10 Autoren einfügen
    authors = [
        ("Alice", "Anderson"),
        ("Bob", "Brown"),
        ("Carol", "Clark"),
        ("David", "Davis"),
        ("Eve", "Evans"),
        ("Frank", "Foster"),
        ("Grace", "Green"),
        ("Hank", "Hill"),
        ("Ivy", "Irwin"),
        ("Jack", "Johnson")
    ]
    cursor.executemany("INSERT INTO author (firstname, lastname) VALUES (?, ?)", authors)

    # 50 Bücher mit zufälligen Publishern einfügen
    for i in range(50):
        isbn = f"978-0-00-{1000000 + i}"
        title = f"Book Title {i+1}"
        pages = random.randint(100, 1000)
        price = round(random.uniform(10, 100), 2)
        publisher_id = random.randint(1, 3)
        cursor.execute(
            "INSERT INTO book (isbn, title, pages, price, publisher_id) VALUES (?, ?, ?, ?, ?)",
            (isbn, title, pages, price, publisher_id)
        )
        # 1–3 zufällige Autoren pro Buch zuordnen
        author_ids = random.sample(range(1, 11), random.randint(1, 3))
        for author_id in author_ids:
            cursor.execute(
                "INSERT INTO book_author (book_isbn, author_id) VALUES (?, ?)",
                (isbn, author_id)
            )
def main():
    conn = sqlite3.connect(":memory:")
    prepare(conn)
    conn.close()  

if __name__ == '__main__':
    main()
