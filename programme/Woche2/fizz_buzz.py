ITERATION_START = 11
ITERATION_END = 47
ITERATION_STEP = 1

FIRST_DIVIDER = 3
SECOND_DIVIDER = 7

FIRST_DIVIDER_MESSAGE = "Fiz"
SECOND_DIVIDER_MESSAGE = "Buz"

BOTH_DIVIDER_MESSAGE = FIRST_DIVIDER_MESSAGE + SECOND_DIVIDER_MESSAGE

number = ITERATION_START
while number <= ITERATION_END:
    first_dividable = False
    second_dividable = False
    if number % FIRST_DIVIDER == 0:
        first_dividable = True
    if number % SECOND_DIVIDER == 0:
        second_dividable = True

    if first_dividable and second_dividable:
        print(f'{BOTH_DIVIDER_MESSAGE}')
    elif first_dividable:
        print(f'{FIRST_DIVIDER_MESSAGE}')
    elif second_dividable:
        print(f'{SECOND_DIVIDER_MESSAGE}')
    else:
        print(f'{number}')
    number += ITERATION_STEP    

