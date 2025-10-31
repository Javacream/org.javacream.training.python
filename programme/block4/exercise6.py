from datetime import datetime as calendar

def get_date_and_time():
    actual_datetime = calendar.now()
    actual_date = actual_datetime.date()
    actual_time = actual_datetime.time()
    return actual_date, actual_time

def main():
    datetime = get_date_and_time()
    # date = datetime[0]
    # time = datetime[1]
    date, time = datetime
    print(f'Date: {date}, time:{time}')
main()