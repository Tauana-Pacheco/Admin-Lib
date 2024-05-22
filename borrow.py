from db import create_connection, close_connection
# from books import DigitalBook
# from user import User

class Borrow: 
    def __init__(self, status, start_date, end_date, id_user, id_book):
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.id_user = id_user
        self.id_book = id_book
        self.borrowed_books = [] 
        self.reserved_books = []
        self.returned_books = []
        self.loads = []
    
    def save_to_db(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Borrow (status, start_date, end_date, id_user, id_book) VALUES (?, ?, ?, ?, ?)", 
            (self.status, self.start_date, self.end_date, self.id_user, self.id_book))
            connection.commit()
            cursor.close()
            close_connection(connection)
            print(f"Emprestimo realizado para: {self.id_user}, livro {self.id_book} salvo no banco de dados.")
    
    # Getters
    def get_status(self):
        return self.status

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_id_user(self):
        return self.id_user

    def get_id_book(self):
        return self.id_book

    # Setters
    def set_status(self, status):
        self.status = status

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_id_user(self, id_user):
        self.id_user = id_user

    def set_id_book(self, id_book):
        self.id_book = id_book
    
    def check_available(self, book):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT available FROM Book WHERE id = ?", (book.id,))
            book_available = cursor.fetchone()
            if not book_available:
                print("O livro está indisponível no momento.")
            elif book.id in self.reserved_books:
                print("O livro já está reservado por você.")
            else:
                print("O livro está disponível para empréstimo.")
            cursor.close()
            close_connection(connection)

    # def returned_book(self, book):
    #     connection = create_connection()
    #     if connection:
    #         cursor = connection.cursor()
    #         cursor.execute("SELECT available FROM Book WHERE id = ?", (book.id,))
    #         book_available = cursor.fetchone()
    #         if not book_available:
    #             cursor.execute("UPDATE Book SET available = TRUE WHERE id = ?", (book.id,))
    #             cursor.execute("DELETE FROM Borrow WHERE id_book = ?", (book.id,))
    #             if book.id in self.borrowed_books:
    #                 self.borrowed_books.remove(self.id_book)
    #                 self.returned_books.append(book.id)
    #                 print(f"O livro '{book.id}' foi devolvido com sucesso.")
    #             else:
    #                 print(f"Erro: o livro '{book.id}' não está na lista de livros emprestados.")
    #         else:
    #             print(f"O livro '{book.id}' não está emprestado pelo usuário.")
    #         cursor.close()
    #         close_connection(connection)
    def returned_book(self, book):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT available FROM Book WHERE id = ?", (book.id,))
            result = cursor.fetchone()
            if result is not None:
                book_available = result[0]
                if not book_available:
                    cursor.execute("UPDATE Book SET available = TRUE WHERE id = ?", (book.id,))
                    cursor.execute("DELETE FROM Borrow WHERE id_book = ?", (book.id,))
                    connection.commit()
                    if book.id in self.borrowed_books:
                        self.borrowed_books.remove(book.id)
                        self.returned_books.append(book.id)
                        print(f"O livro '{book.id}' foi devolvido com sucesso.")
                    else:
                        print(f"Erro: o livro '{book.id}' não está na lista de livros emprestados.")
                else:
                    print(f"O livro '{book.id}' não está emprestado pelo usuário.")
            else:
                print("Livro não encontrado.")
            cursor.close()
            close_connection(connection)

    def reserve_book(self, book):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT available FROM Book WHERE id = ?", (book.id,))
            result = cursor.fetchone()
            if result:
                book_available = result[0]
                if not book_available:
                    print("O livro está indisponível no momento.")
                elif book.id in self.reserved_books:
                    print("O livro já está reservado por você.")
                else:
                    cursor.execute("SELECT available FROM User WHERE id = ?", (self.id_user,))
                    user_result = cursor.fetchone()
                    if user_result:
                        user_available = user_result[0]
                        if not user_available:
                            print("O usuário não pode reservar livros no momento.")
                        else:
                            cursor.execute("UPDATE Book SET available = FALSE WHERE id = ?", (book.id,))
                            cursor.execute("INSERT INTO Borrow (status, start_date, end_date, id_user, id_book) VALUES (?, ?, ?, ?, ?)",
                                           ('RESERVADO', self.start_date, self.end_date, self.id_user, book.id))
                            connection.commit()
                            self.reserved_books.append(book.id)
                            print("Reserva realizada com sucesso.")
                    else:
                        print("Usuário não encontrado.")
            else:
                print("Livro não encontrado.")
            cursor.close()
            close_connection(connection)

