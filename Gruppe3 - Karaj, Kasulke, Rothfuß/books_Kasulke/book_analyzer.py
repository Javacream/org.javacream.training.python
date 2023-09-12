from book_data_processor import BookDataProcessor

class BookAnalyzer(BookDataProcessor):
    def __init__(self, input_file="E:\\VS_CODE\Buecher\_books.csv"):
        super().__init__(input_file)
        self.data_processor = BookDataProcessor(input_file)
        self.titles_with_python_file = "E:\\VS_CODE\Buecher\_titleswithpy.csv"
        self.expensive_books_file = "E:\\VS_CODE\Buecher\_expensive_books.csv"
        self.average_books_file = "E:\\VS_CODE\Buecher\_average_books.csv"
        self.minmax_title_file = "E:\\VS_CODE\Buecher\_minmax_title.csv"

    def filter_titles_with_python(self):
        python_in_title_data = [row for row in self.data_processor.data if "python" in row["Title"].lower()]
        self.data_processor.write_csv(python_in_title_data, self.titles_with_python_file)

    def filter_expensive_books(self):
        expensive_books_data = [row for row in self.data_processor.data if float(row["Price"]) > 50]
        self.data_processor.write_csv(expensive_books_data, self.expensive_books_file)

    def calculate_average_price(self):
        total_price = sum(float(row["Price"]) for row in self.data_processor.data)
        average_price = total_price / len(self.data_processor.data)
        with open(self.average_books_file, "w") as file:
            file.write("Average Price\n")
            file.write(f"{average_price:.2f}\n")

    def find_minmax_titles(self):
        shortest_title = min(self.data_processor.data, key=lambda x: len(x["Title"]))
        longest_title = max(self.data_processor.data, key=lambda x: len(x["Title"]))
        with open(self.minmax_title_file, "w") as file:
            file.write("Shortest Title,Longest Title\n")
            file.write(f'"{shortest_title["Title"]}", "{longest_title["Title"]}"\n')

    def analyze_books(self):
        self.data_processor.find_duplicate_isbns()
        self.data_processor.create_cleaned_dataset()
        self.filter_titles_with_python()
        self.filter_expensive_books()
        self.calculate_average_price()
        self.find_minmax_titles()
        print("Analysis completed.")


if __name__ == "__main__":
    analyzer = BookAnalyzer()
    analyzer.analyze_books()
