import math
import datetime as dtm
# dtm = datetime
def perimeter(radius):
    # pi_approx = 3.1415
    return 2* radius * math.pi

def actual_date_and_time():
    #dtm = datetime
    return dtm.datetime.now()

def main():
    print(perimeter(2))
    print(actual_date_and_time())
main()