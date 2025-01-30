import file_util
import shopping
def main():
    infile = 'programme/Woche4/demo/shopping_list.txt'
    outfile = 'programme/Woche4/demo/shopping.txt'
    
    raw_data = file_util.read_raw(infile)
    data = file_util.clean_data(raw_data)
    unique_items = shopping.create_unique_items(data)
    shopping_info = shopping.create_shopping_collection(data)
    print(unique_items)
    file_util.write_result(shopping_info, outfile)
if __name__ == '__main__':
    main()