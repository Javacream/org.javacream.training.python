START = 1
END = 30
STEP = 1
CHECK_DIVIDABLE_BY_3 = 3
MESSAGE_DIVIDABLE_BY_3 = 'Fizz'
CHECK_DIVIDABLE_BY_5 = 5
MESSAGE_DIVIDABLE_BY_5 = 'Buzz'
MESSAGE_DIVIDABLE_BY_3_and_5 = 'FizzBuzz'

counter = START
while counter <= END:
    
    dividable_by_3 = counter % CHECK_DIVIDABLE_BY_3 == 0
    dividable_by_5 = counter % CHECK_DIVIDABLE_BY_5 == 0
    dividable_by_3_and_5 = dividable_by_3 and dividable_by_5

    if dividable_by_3_and_5:
        print(MESSAGE_DIVIDABLE_BY_3_and_5)
    elif dividable_by_3:
        print(MESSAGE_DIVIDABLE_BY_3)
    elif dividable_by_5:
        print(MESSAGE_DIVIDABLE_BY_5)
    else:    
        print(counter)
    counter += STEP