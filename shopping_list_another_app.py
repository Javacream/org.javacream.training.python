import shopping_list

def main():
    path = "shopping_list.txt"
    rows = shopping_list.read_shopping_list(path)
    print(rows)
main()