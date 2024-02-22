import datetime

def main():
    actual_date = datetime.datetime.now()
    second_of_april_2024 = datetime.datetime(2024, 4, 2) # siehe https://www.w3schools.com/python/python_datetime.asp
    print(second_of_april_2024)
    # Berechnungen mit Datumswerten
    print (f"actual_data vor 2.4.2024? {actual_date < second_of_april_2024}")
    delta = datetime.timedelta(days=1)
    print (f"tag nach 2.4.2024? {second_of_april_2024 + delta}")

main()