import books

def write_result(filename, result):
    with open(filename, "w") as file:
        text_str = "{},{},{}\n"
        for element in result:
            file.write(text_str.format(element.ISBN, element.title, element.price))
            
def cleanup(bookmanager: books.BookManager):
    duplicates = bookmanager.find_duplicate_isbn()
    result = list()
    for element in duplicates:
        key_element = bookmanager.find_by_ISBN(element)
        for key in key_element:
            result.append(bookmanager.books.get(key))
            bookmanager.books.pop(key)
    write_result("duplicate_isbns.txt", result)
    write_result("books_cleanedup.txt", bookmanager.books.values())
    
def analyse(bookmanager: books.BookManager):
    title_match = bookmanager.find_by_title("Python")
    write_result("python_books.txt", title_match)
    price_match = bookmanager.find_by_price(50)
    write_result("expensive_books.txt", price_match)
    # calculate average price of books
    price_sum = 0
    counter = 0
    for books in bookmanager.books.values():
        counter += 1
        price_sum += books.price
    average_price = round( price_sum / counter, 2)
    with open("average_book_price.txt", "w") as file:
        file.write(str(average_price))
    # find books with shortest and longest title
    list_of_titles = [books.title for books in bookmanager.books.values()]
    list_of_titles.sort(key = len)
    min_length = len(list_of_titles[0])
    max_length = len(list_of_titles[-1])
    length_match = bookmanager.find_by_title_length(min_length) + bookmanager.find_by_title_length(max_length)
    write_result("min_max.txt", length_match)
    
def main():                
    book_manager = books.BookManager("books.csv")
    cleanup(book_manager)
    analyse(book_manager)

main()