def step1():
    step_var = 'Hugo'
    print(f'step1 wurde aufgerufen, {step_var}')

def step3():
    step_var = 'Fritz'
    print(f'step1 wurde aufgerufen, {step_var}')

def step2():
    name = 'Emil'
    print(f'step1 wurde aufgerufen, {name}')

def main():
    name = 'Sawitzki'
    main_var = 42
    main_var2 = True
    step1()
    step2()
    step3()
main()