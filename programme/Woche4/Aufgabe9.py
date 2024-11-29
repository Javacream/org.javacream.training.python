def square(numbers: list):
    return [(number, number*number) for number in numbers]

def main():
    number_list = [1,7,-5,2]
    print(square(number_list))

main()