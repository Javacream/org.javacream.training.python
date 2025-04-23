import sqlite3

def main():
  conn = sqlite3.connect(':memory:')
  
  cursor = conn.cursor()
  
  cursor.execute('''
  CREATE TABLE users (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER
  )
  ''')
  
  users = [
      ("Alice", 30),
      ("Bob", 25),
      ("Charlie", 35)
  ]
  cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users)
  
  conn.commit()
  
  cursor.execute('SELECT * FROM users')
  rows = cursor.fetchall()
  
  for row in rows:
      print(row)
  
  conn.close()

main()
