class Book:
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.str_template = "Book: isbn={}, title={}, price={}"

    def __str__(self):
        return self.str_template.format(self.isbn, self.title, self.price)


class BooksManager:
    def __init__(self):
        self.books = {}
        self.clean_books = {}
        self.dpl_books = {}
        self.books_count = 0
        self.clean_books_count = 0
        self.dpl_books_count = 0
        self.__load_books__()

    def __load_books__(self):
        with open("books.csv", "r") as f:
            for line in f.readlines():
                isbn, title, price = line.strip().split(",")
                if price.isnumeric():
                    price = int(price)
                    new_book = Book(isbn, title, price)
                    self.books[self.books_count] = new_book
                    self.books_count += 1

    # remove duplicates from dictionary
    def remove_duplicates(self):     
        # iterate the dictionary and find isbn duplicates
        found = 0
        exist = False
        self.clean_books = self.books.copy()
        self.clean_books_count = self.books_count
        for i in self.books:
            for j in self.books:
                if i!= j and self.books[i].isbn == self.books[j].isbn:
                    if not self.check_title_in_dict(self.dpl_books, self.books[i].title):  # if isbn is not in dpl_books           
                        self.dpl_books[self.dpl_books_count] = self.books[j]               # add book to dpl_books
                        self.dpl_books_count += 1
                    if j in self.clean_books:
                         del self.clean_books[j]                                           # delete book from clean_books
                    self.clean_books_count -= 1
                    found += 1
            # if a duplicate was found before add it in duplicate dict if not already exist
            if found:
                if not self.check_title_in_dict(self.dpl_books, self.books[i].title):         
                    self.dpl_books[self.dpl_books_count] = self.books[i]
                    self.dpl_books_count += 1
                 # delete book from clean_books if still there
                if i in self.clean_books:
                    del self.clean_books[i]                                               
                    self.clean_books_count -= 1
                found = 0
        return self.clean_books, self.dpl_books
   
    # check for title in books dictionary
    def check_title_in_dict(self, dict, title):
        check = False
        for i in dict:
            if dict[i].title == title:
                #print("duplicates: ", dict[i].isbn, dict[i].title, dict[i].price)
                check = True
        return check
      
    def show_books(self):
        for book in self.books:
            print(self.books[book].isbn, self.books[book].title, self.books[book].price)

    def show_books_clean(self):
        for book in self.clean_books:
            print("      ",self.clean_books[book].isbn, self.clean_books[book].title, self.clean_books[book].price)

    def show_books_dpl(self):
        for book in self.dpl_books:
            print("      ",self.dpl_books[book].isbn, self.dpl_books[book].title, self.dpl_books[book].price)

    def search_in_title(self, keyword): # search for keyword in titles in dictionary dict
        return [book for book in self.clean_books.values() if keyword in book.title] 
    
    # search for books with higher price than parameter
    def search_higher_price(self, price):
        return [book for book in self.clean_books.values() if price < book.price]

    # find the average price of all books and return it
    def average_price(self):
        return sum(book.price for book in self.clean_books.values()) / len(self.clean_books.values())
    
    # function to find in clean_books dictionary the book with the larger title and the smaller title
    def find_min_max_title(self):
        longer_title = []
        shorter_title = []

        max_key = next(iter(self.clean_books))
        min_key = next(iter(self.clean_books))
        for i in self.clean_books:
            if len(self.clean_books[i].title) > len(self.clean_books[max_key].title):
                max_key = i
                longer_title = []
                longer_title.append(self.clean_books[i])
            elif len(self.clean_books[i].title) < len(self.clean_books[max_key].title): 
                if len(self.clean_books[i].title) < len(self.clean_books[min_key].title):
                    min_key = i
                    shorter_title = []
                    shorter_title.append(self.clean_books[i])
                elif len(self.clean_books[i].title) == len(self.clean_books[min_key].title):
                    shorter_title.append(self.clean_books[i])
            elif len(self.clean_books[i].title) == len(self.clean_books[max_key].title):
                longer_title.append(self.clean_books[i])
                if len(self.clean_books[i].title) == len(self.clean_books[min_key].title):
                    shorter_title.append(self.clean_books[i])
            elif len(self.clean_books[i].title) == len(self.clean_books[min_key].title):
                shorter_title.append(self.clean_books[i])
        
        min_max = [*shorter_title, *longer_title]  # create a list of all the books with the larger title and the smaller title
        return min_max
    
def write_result(filename, books):
    with open(filename, 'w') as file:
        if type(books) == float:
            file.write(str(f'{books: .2f}'))
            return
        for book in books:
            #print(str(book))
            file.write(str(book) + '\n')  
''' 
def main():
    
    lib = BooksManager()  
    
    lib.remove_duplicates()
    #lib.show_books_clean()
    print(f"Loaded: {len(lib.books)} books in Total:")
    print("===========================")   
    print(f" ##### Loaded: {len(lib.clean_books)} books w/out duplicates")
    print(f" ##### found: {len(lib.dpl_books)} isbn with duplicates:")
    lib.show_books_dpl()
   
    average_price = lib.average_price() 
    print(f"Average price: {average_price:.2f}")   
    write_result("average_book_price.txt", average_price)

    larger_title, shorter_title = lib.find_larger_title() 
    print(f"Largest book: {len(larger_title)}")
    if len(larger_title):
        write_result("max_title.txt", larger_title)
    print(f"Smallest book: {len(shorter_title)}")
    if len(shorter_title):
        write_result("min_title.txt", shorter_title)
    
    #min_max = shorter_title.extend(larger_title)
    min_max = [*shorter_title, *larger_title]
    print(f"Largest list: {len(min_max)}")
    write_result("min_max.txt",min_max)

    # search for keyword in titles
    search_keyword = input("Search for keyword: ")
    print("--------------------------")
    result = lib.search_in_title(search_keyword)
    print ("Found results: ",len(result))
    print("====================")       
    write_result("python_books.txt", result)
       
    # search for books with higher price than parameter
    search_price = int(input("Search for price: "))
    print("--------------------------")
    result = lib.search_higher_price(search_price)
    print ("Found results: ",len(result))
    print("====================")
    write_result("expensive_books_txt", result)
 
if __name__ == "__main__":
    main()
'''