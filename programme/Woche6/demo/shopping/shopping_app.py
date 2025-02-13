import file_util
import database_util
import shopping
def main():
    #infile = 'programme/Woche4/demo/shopping_list.txt'
    outfile = 'programme/Woche6/demo/shopping/shopping.txt'
    data = database_util.read_shopping_list()
    # data = database_util.read_shopping_list_for('Sawitzki')
    unique_items = shopping.create_unique_items(data)
    shopping_info = shopping.create_shopping_collection(data)
    print(unique_items)
    file_util.write_result(shopping_info, outfile)
if __name__ == '__main__':
    main()