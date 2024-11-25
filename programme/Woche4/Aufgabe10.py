def flatten_one_hierarchy(data: list):
    return [element for sublist in data for element in sublist ]

def main():
    data = [[1,7],[-5,2, 8, 19], [3], [4,2,6]]
    print(flatten_one_hierarchy(data))

main()