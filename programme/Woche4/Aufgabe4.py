def min_max_of_numbers(numbers):
    min_of_numbers = min(numbers)
    max_of_numbers = max(numbers)
    # return (min_of_numbers, max_of_numbers)
    # oder vielleicht ein dict?
    return {'min': min_of_numbers, 'max': max_of_numbers}
def main():
    print(min_max_of_numbers([2,7,-5,33]))

main()