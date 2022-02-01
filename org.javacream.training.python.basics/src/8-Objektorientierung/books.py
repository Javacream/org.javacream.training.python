class Book(object):
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title

    def info(self):
        return "Book: isbn=%s, title=%s" % (self.isbn, self.title)

class SchoolBook(Book):

    def __init__(self, isbn, title, year, subject):
        Book.__init__(self, isbn, title)
        self.year = year
        self.subject = subject

class SpecialistBook(Book):

    def __init__(self, isbn, title, topic):
        Book.__init__(self, isbn, title)
        self.topic = topic
