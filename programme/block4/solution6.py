import datetime as dt

def actual():
    actual = dt.datetime.now()
    actual_date = actual.date()
    actual_time = actual.time()
    return actual_date, actual_time
def main():
    date, time  = actual()
    print(date)
    print(time)

main()