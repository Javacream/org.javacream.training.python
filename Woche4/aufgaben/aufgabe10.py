def main():
    def flatten_list(two_dimensional_list):
        return [item for sublist in two_dimensional_list for item in sublist ]

    data = [["A", "B"], ["F", "O", "I"], ["X", "Y", "Z"]]
    print(flatten_list(data))

main()