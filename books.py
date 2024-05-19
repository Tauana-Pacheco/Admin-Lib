class Book:
    def __init__(self, id, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages):
        self.id = id
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.num_of_editions = num_of_editions 
        self.num_of_copies = num_of_copies
        self.num_of_pages = num_of_pages
    
     # Getters
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year_of_publication(self):
        return self.year_of_publication

    def get_num_of_editions(self):
        return self.num_of_editions

    def get_num_of_copies(self):
        return self.num_of_copies

    def get_num_pages(self):
        return self.num_pages

    # Setters
    def set_id(self, id):
        self.id = id

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_year_of_publication(self, year_of_publication):
        self.year_of_publication = year_of_publication

    def set_num_of_editions(self, num_of_editions):
        self.num_of_editions = num_of_editions

    def set_num_of_copies(self, num_of_copies):
        self.num_of_copies = num_of_copies

    def set_num_pages(self, num_pages):
        self.num_pages = num_pages

    def show_info_book(self):
        print(f"Titulo: {self.title}")
        print(f"Autor: {self.author}") 
        print(f"Ano de publicação: {self.year_of_publication}") 
        print(f"Número de edição: {self.num_of_editions}")
        print(f"Número de exemplares: {self.num_of_copies}")

class PhysicalBook(Book):
    def __init__(self, id, title, author,  cover_type,year_of_publication, num_of_editions, num_of_copies, num_of_pages):
        super().__init__(id, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages)
        self.cover_type = cover_type
    
    def show_info_book(self):
        super().show_info_book()
        print(f"Tipo de capa: {self.cover_type}") 


# Livros fisícos
book = PhysicalBook('Kindred', 'Octavia Buttler', 1990, 'capa dura', 10, 5, 3, 205)
book.show_info_book()

class DigitalBook(Book):
    def __init__(self, id, title, author, file_size, year_of_publication, num_of_editions, num_of_copies, num_of_pages):
        super().__init__(id, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages)
        self.file_size = file_size

    def show_info_book(self):
        super().show_info_book()
        print(f"Tamanho do arquivo: {self.file_size}") 


# Livros digitais
# book = DigitalBook('Kindred', 'Octavia Buttler', 1990, '150gb', 10, 5, 3)
# book.show_info_book()
