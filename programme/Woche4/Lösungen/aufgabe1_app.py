import aufgabe1_service as sum_up
def main():
    numbers = [1, 5, -5, 23, 666]
    sum_of_numbers = sum_up.sum_list(numbers)
    print(f"Die Summe der Liste {numbers} ist {sum_of_numbers}")

if __name__ == '__main__':
    main()