import file_util
import shopping
def main():
    raw_data = file_util.read_raw('shopping_list.txt')
    data = file_util.clean_data(raw_data)
    unique_items = shopping.create_unique_items(data)
    shopping_info = shopping.create_shopping_collection(data)
    print(unique_items)
    file_util.write_result(shopping_info, 'shopping.txt')
if __name__ == '__main__':
    main()