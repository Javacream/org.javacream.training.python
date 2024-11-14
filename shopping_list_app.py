from shopping_list_library import *
def main():
    raw_shopping_list_path = './data/raw_shopping_list.txt'
    shopping_list_path = './data/shopping_list.txt'
    items = get_items(raw_shopping_list_path)
    shopping_list = create_shopping_list(items)
    write_shopping_list_to(shopping_list_path, shopping_list)


if __name__ == '__main__':
    main()