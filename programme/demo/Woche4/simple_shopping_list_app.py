import shopping_list

def main():
    shopping_entries = shopping_list.read_raw_shopping_list()
    shopping_entries = shopping_list.remove_end_of_line(shopping_entries)
    print(shopping_entries)

if __name__ == '__main__':
    main()