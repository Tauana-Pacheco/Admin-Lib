from books import Book

class Borrow: 
    def __init__(self, status, start_date, end_date, user_name, book_name):
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.user_name = user_name
        self.book_name = book_name
        self.borrowed_books = [] 
        self.reserved_books = []
        self.returned_books = []
        self.loads = []
    
    # Getters
    def get_status(self):
        return self.status

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_user_name(self):
        return self.user_name

    def get_id_book(self):
        return self.id_book

    # Setters
    def set_status(self, status):
        self.status = status

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_id_book(self, id_book):
        self.id_book = id_book
    
    # Verifica disponibilidade do livro
    def check_available(self, books):
        if books in self.borrowed_books:
            print("O livro está indisponível no momento.")
        elif books in self.reserved_books:
            print("O livro já está reservado por você.")
        else:
            print("O livro está disponível para empréstimo.")
    
    # Devolve Livro
    def returned_book(self, returned_books):
        for book in returned_books:
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
                print(f"O livro '{book}' foi devolvido com sucesso.")
            else:
                print(f"O livro '{book}' não está emprestado pelo usuário.")

    # Reserva livro
    def reserve_book(self, books):
        if books in self.borrowed_books:
            print("O livro está indisponível no momento.")
        elif books in self.reserved_books:
            print("O livro já está reservado por você.")
        else:
            if self.status == 'INDISPONÍVEL':
                print("O livro está indisponível no momento.")
            else:
                self.reserved_books.append(books)
                print("Reserva realizada com sucesso.")
    