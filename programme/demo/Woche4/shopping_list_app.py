import shopping_list as sl
def main():
    raw_shopping_list = sl.read_raw_shopping_list()
    cleaned_raw_shopping_list = sl.remove_end_of_line(raw_shopping_list)
    shopping_list = sl.create_shopping_list(cleaned_raw_shopping_list)
    sl.write_shopping_list(shopping_list)

if __name__ == '__main__':
    main()


