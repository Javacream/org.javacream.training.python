class BookDataProcessor:
    def __init__(self, input_file="E:\\VS_CODE\Buecher\_books.csv"):
        self.input_file = input_file
        self.data = self.read_csv(input_file)
        self.dupe_file = "E:\\VS_CODE\Buecher\_duplicates.csv"
        self.cleaned_file = "E:\\VS_CODE\Buecher\_books_cleaned.csv"

    def read_csv(self, file_name):
        data = []
        with open(file_name, "r") as file:
            lines = file.readlines()
            header = lines[0].strip().split(",")
            for line in lines[1:]:
                values = line.strip().split(",")
                data.append(dict(zip(header, values)))
        return data

    def write_csv(self, data, file_name):
        with open(file_name, "w") as file:
            if data:
                header = data[0].keys()
                file.write(",".join(header) + "\n")
                for row in data:
                    values = [str(row[key]) for key in header]
                    file.write(",".join(values) + "\n")

    def find_duplicate_isbns(self):
        isbn_count = {}
        duplicate_data = []
        for row in self.data:
            isbn = row["ISBN"]
            if isbn in isbn_count:
                isbn_count[isbn] += 1
            else:
                isbn_count[isbn] = 1

        for row in self.data:
            isbn = row['ISBN']
            if isbn_count[isbn] > 1:
                duplicate_data.append(row)

        self.write_csv(duplicate_data, self.dupe_file)

    def create_cleaned_dataset(self):
        unique_data = []
        seen_isbns = set()
        for row in self.data:
            isbn = row["ISBN"]
            if isbn not in seen_isbns:
                unique_data.append(row)
                seen_isbns.add(isbn)

        self.write_csv(unique_data, self.cleaned_file)
