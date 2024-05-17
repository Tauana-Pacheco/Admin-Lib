class Book:
    def __init__(self, id, title, author, year_of_publication, num_of_editions, num_of_copies):
        self.id = id
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.num_of_editions = num_of_editions 
        self.num_of_copies = num_of_copies
        # add num page
        # add num books

    def show_info_book(self):
        print(f"Titulo: {self.title}")
        print(f"Autor: {self.author}") 
        print(f"Ano de publicação: {self.year_of_publication}") 
        print(f"Número de edição: {self.num_of_editions}")
        print(f"Número de exemplares: {self.num_of_copies}")

class PhysicalBook(Book):
    def __init__(self, id, title, author,  cover_type,year_of_publication, num_of_editions, num_of_copies):
        super().__init__(id, title, author, year_of_publication, num_of_editions, num_of_copies)
        self.cover_type = cover_type
    
    def show_info_book(self):
        super().show_info_book()
        print(f"Tipo de capa: {self.cover_type}") 


# Livros fisícos
book = PhysicalBook('Kindred', 'Octavia Buttler', 1990, 'capa dura', 10, 5, 3)
book.show_info_book()

class DigitalBook(Book):
    def __init__(self, id, title, author, file_size, year_of_publication, num_of_editions, num_of_copies):
        super().__init__(id, title, author, year_of_publication, num_of_editions, num_of_copies)
        self.file_size = file_size

    def show_info_book(self):
        super().show_info_book()
        print(f"Tamanho do arquivo: {self.file_size}") 


# Livros digitais
# book = DigitalBook('Kindred', 'Octavia Buttler', 1990, '150gb', 10, 5, 3)
# book.show_info_book()
