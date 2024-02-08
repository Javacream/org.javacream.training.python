def main():
    def square_number_tuples(n):
        return [(i, i*i) for i in range(1, n+1)]
    n = 3
    print(square_number_tuples(n))

main()