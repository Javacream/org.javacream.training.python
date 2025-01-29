def step1(person_name = 'Andrea'):
    step_var = 'Hugo'
    print(f'step1 wurde aufgerufen, {step_var}, {person_name}')


def step3(number): # implizit erfolgt hier eine Zuweisung number = main_var
    step_var = 'Fritz'
    print(f'step1 wurde aufgerufen, {step_var} {number}')

def step2():
    name = 'Emil'
    print(f'step1 wurde aufgerufen, {name}')

def main():
    name = 'Sawitzki'
    main_var = 42
    main_var2 = True
    step1()
    step1("Helga")
    step1(name)
    step2()
    # step3()
    step3(main_var)
main()