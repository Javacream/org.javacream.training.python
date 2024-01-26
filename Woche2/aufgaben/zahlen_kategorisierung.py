START_NUMBER = 1
END_NUMBER = 30
FIRST_DIVISOR = 4
SECOND_DIVISOR = 5
MESSAGE_FOR_FIRST_DIVISOR = "Fizz"
MESSAGE_FOR_SECOND_DIVISOR = "Buzz"
MESSAGE_FOR_FIRST_AND_SECOND_DIVISOR = "FizzBuzz"

counter = START_NUMBER
while (counter <= END_NUMBER):
    if (counter % FIRST_DIVISOR == 0) and (counter % SECOND_DIVISOR > 0):
        print(f"{counter}, {MESSAGE_FOR_FIRST_DIVISOR}")
    elif (counter % FIRST_DIVISOR > 0) and (counter % SECOND_DIVISOR == 0):
        print(f"{counter}, {MESSAGE_FOR_SECOND_DIVISOR}")
    elif (counter % FIRST_DIVISOR == 0) and (counter % SECOND_DIVISOR == 0):
        print(f"{counter}, {MESSAGE_FOR_FIRST_AND_SECOND_DIVISOR}")
    else:
        print(f"{counter}")
    counter += 1