def sum_of_numbers(*numbers): # * macht imlizit aus der Parameterliste im Aufruf eine Python-Liste
    result = sum(numbers)
    return result

def application():
    # Lösung mit varargs
    result_sum_of_numbers = sum_of_numbers(2,3,4,5,6) 
    print(result_sum_of_numbers)

application()