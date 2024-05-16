class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

class PhysicalBook(Book):
    def __init__(self, id, title, author, size):
        super().__init__(id, title, author)
        self.size = size
        
        
class DigitalBook(Book):
    def __init__(self, id, title, author, cover_type, file_size):
        super().__init__(id, title, author)
        self.cover_type = cover_type
        self.file_size = file_size