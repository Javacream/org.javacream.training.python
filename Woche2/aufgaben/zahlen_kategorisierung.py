counter = 1
while (counter <= 30):
    if (counter % 3 == 0) and (counter % 5 > 0):
        print(f"{counter}, Fizz")
    elif (counter % 3 > 0) and (counter % 5 == 0):
        print(f"{counter}, Buzz")
    elif (counter % 3 == 0) and (counter % 5 == 0):
        print(f"{counter}, FizzBuzz")
    else:
        print(f"{counter}")
    counter += 1