import redshift_connector

# Verbindung zu Amazon Redshift herstellen
conn = redshift_connector.connect(
    host='your-cluster-name.region.redshift.amazonaws.com',
    database='your_database_name',
    user='your_username',
    password='your_password',
    port=5439
)

# Cursor erstellen und SQL-Abfrage ausführen
cursor = conn.cursor()
cursor.execute("SELECT current_date;")

# Ergebnis abrufen
result = cursor.fetchall()
print("Ergebnis:", result)

# Verbindung schließen
cursor.close()
conn.close()
