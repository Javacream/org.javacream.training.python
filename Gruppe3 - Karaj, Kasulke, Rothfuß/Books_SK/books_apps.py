import sys
import books

def main():

    try:
        args = sys.argv
        #search_keyword = args[1]
        #lowest_price = args[2]
        
        book_manager = books.BooksManager()
        book_manager.remove_duplicates()
        print(f"Loaded: {len(book_manager.books)} books in Total:")
        print(f" ##### Loaded: {len(book_manager.clean_books)} books w/out duplicates")
 
        print(f" ##### Found: {len(book_manager.dpl_books)} isbn with duplicates:")
        book_manager.show_books_dpl()

        books.write_result("python_books.txt", book_manager.search_in_title("Python"))
        books.write_result("expensive_books_txt", book_manager.search_higher_price(50))
        books.write_result("average_book_price.txt", book_manager.average_price())
        books.write_result("min_max_title.txt", book_manager.find_min_max_title())
    except Exception as e:
        print (str(e))    

main()