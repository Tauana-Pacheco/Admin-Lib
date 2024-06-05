from db import  drop_table, delete_table, create_tables, create_connection, close_connection
class Book:
    def __init__(self, isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, type_book, id_=None):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.num_of_editions = num_of_editions 
        self.num_of_copies = num_of_copies
        self.num_of_pages = num_of_pages
        self.available = True
        self.type_book = type_book
        self.id = id_

    def save_to_db(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO Book (isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, available, type_book) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (self.isbn, self.title, self.author, self.year_of_publication, self.num_of_editions, self.num_of_copies, self.num_of_pages, self.available, self.type_book))
                book_id = cursor.lastrowid 
                
                if isinstance(self, PhysicalBook):
                    cursor.execute("INSERT INTO PhysicalBook (id, cover_type, weight) VALUES (?, ?, ?)",
                                    (book_id, self.cover_type, self.weight))
                elif isinstance(self, DigitalBook):
                    cursor.execute("INSERT INTO DigitalBook (id, file_size, format) VALUES (?, ?, ?)",
                                    (book_id, self.file_size, self.format))

                connection.commit()
                print(f"Livro {self.title} do autor {self.author} foi salvo no banco.")
            except Exception as e:
                print(f"Erro ao salvar livro no banco de dados: {e}")
            finally:
                cursor.close()
                close_connection(connection)


    def update_in_db(self):
         connection = create_connection()
         if connection:
             cursor = connection.cursor()

             cursor.execute("UPDATE Book SET isbn = ?, title = ?, author = ?, year_of_publication = ?, num_of_editions = ?, num_of_copies = ?, num_of_pages = ?, available = ?, type_book = ? WHERE id = ?",
                         (self.isbn, self.title, self.author, self.year_of_publication, self.num_of_editions, self.num_of_copies, self.num_of_pages, self.available, self.type_book, self.id))

             if isinstance(self, PhysicalBook):
                 cursor.execute("UPDATE PhysicalBook SET cover_type = ?, weight = ? WHERE id = ?",
                             (self.cover_type, self.weight, self.id))

             connection.commit()
             cursor.close()
             close_connection(connection)
             print(f"Livro '{self.title}' do autor {self.author} foi atualizado no banco.")

    # Getters
    def get_isbn(self):
        return self.isbn
    
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
    def set_isbn(self, isbn):
        self.isbn = isbn

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

    def get_info_book(self):
        print(f"Titulo: {self.title}")
        print(f"Autor: {self.author}") 
        print(f"Ano de publicação: {self.year_of_publication}") 
        print(f"Número de edição: {self.num_of_editions}")
        print(f"Número de exemplares: {self.num_of_copies}")

class PhysicalBook(Book):
    def __init__(self, isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, cover_type, weight, id_=None):
        super().__init__(isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, 'PhysicalBook', id_)
        self.cover_type = cover_type
        self.weight = weight
    
    def save_to_db(self):
        super().save_to_db()
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO PhysicalBook (id, cover_type, weight) VALUES (?, ?, ?)",
                                (self.id, self.cover_type, self.weight))
                connection.commit()
                print(f"Livro Físico {self.title} do autor {self.author} foi salvo no banco.")
            except Exception as e:
                print(f"Erro ao salvar livro fisico no banco de dados: {e}")
            finally:
                cursor.close()
                close_connection(connection)

    
    def get_info_book(self):
        super().get_info_book()
        print(f"Tipo de capa: {self.cover_type}") 
    
    def get_weight(self):
        super().get_info_book()
        print(f"Peso do livro: {self.weight}") 
    
    def set_cover_type(self, cover_type):
        self.cover_type = cover_type

    def set_weight(self, weight):
        self.weight = weight


class DigitalBook(Book):
    def __init__(self,isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages,  file_size, format, id_=None):
            super().__init__(isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages, 'DigitalBook', id_)
            self.file_size = file_size
            self.format = format

    def get_info_book(self):
        super().get_info_book()
        print(f"Tamanho do arquivo: {self.file_size}")

    def save_to_db(self):
        super().save_to_db()
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO DigitalBook (id, file_size, format) VALUES (?, ?, ?)",
                                (self.id, self.file_size, self.format))
                connection.commit()
                print(f"Livro Digital {self.title} do autor {self.author} foi salvo no banco.")
            except Exception as e:
                print(f"Erro ao salvar livro digital no banco de dados: {e}")
            finally:
                cursor.close()
                close_connection(connection)
