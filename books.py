class Book:
    def __init__(self, id, title, author, year_of_publication, num_of_editions, num_of_copies):
        self.id = id
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.num_of_editions = num_of_editions 
        self.num_of_copies = num_of_copies


class PhysicalBook(Book):
    def __init__(self, id, title, author,  cover_type,year_of_publication, num_of_editions, num_of_copies):
        super().__init__(id, title, author, year_of_publication, num_of_editions, num_of_copies)
        self.cover_type = cover_type

class DigitalBook(Book):
    def __init__(self, id, title, author, file_size, year_of_publication, num_of_editions, num_of_copies):
        super().__init__(id, title, author, year_of_publication, num_of_editions, num_of_copies)
        self.file_size = file_size

class Loan: 
    def __init__(self, status, start_date, end_date, user_name, book):
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.user_name = user_name
        self.book = book

