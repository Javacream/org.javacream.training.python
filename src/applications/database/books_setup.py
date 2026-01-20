import sqlite3
import random
import string

DB_NAME = "books.db"

def random_isbn():
    # Generate a fake 13-digit ISBN
    return "".join(random.choices(string.digits, k=13))

def random_title(i):
    return f"Book Title {i}"

def random_price():
    return round(random.uniform(5.0, 80.0), 2)

def random_pages():
    return random.randint(50, 1200)

def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            isbn VARCHAR(13) PRIMARY KEY,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            pages INTEGER NOT NULL
        )
    """)

    # Insert 1000 entries
    books = []
    for i in range(1, 1001):
        books.append((
            random_isbn(),
            random_title(i),
            random_price(),
            random_pages()
        ))

    cursor.executemany("""
        INSERT OR IGNORE INTO books (isbn, title, price, pages)
        VALUES (?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()

    print("SQLite database created with 1000 books.")

if __name__ == "__main__":
    main()
