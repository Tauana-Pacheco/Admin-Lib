from datetime import datetime
from borrow import Borrow
from user import User
from books import Book
from employee import Employee

class Librarian(Employee):
  def __init__(self, name, _password, _age, _email, _address, _contact, id_librarian):
    super().__init__(name, _password, _age, _email, _address, _contact)
    self.id_librarian = id_librarian
    self.books = []

  def get_books(self):
     return self.books

  # Empresta livro
  ##### talvez retirar
  def borrow_books(self, books, user):
    if books.available == False:
      print(f"O books '{books.title}' não está disponível para empréstimo.")
      return None
    else: 
      date_borrow = datetime.now().strftime("%Y-%m-%d")
      name = user.get_user_name()
      borrwed = Borrow("emprestado", date_borrow, None, name , 'No seu pescoço')
      print(f"Livro '{books.title}' foi emprestado para {name} em {date_borrow}.")
      return borrwed

  # Adiciona novos Livros 
  def _add_new_books(self, books):
      for book in books:
          self.books.append(book)
      
  # Remove Livros
  def _remove_books(self, books):
     for book in books:
          self.books.remove(book)
  
#  id, isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages
livro = Book('978-3-16-148410-0', "O Senhor dos Anéis", "J.R.R. Tolkien", "123456789", 10, 20, 1000)
usuario = User("Alice", "senha123", 25, "alice@example.com", "123 Main Street", "555-1234", "12345", True)

librarian = Librarian('Maria', 's12345', 22, 'van@gmail.com', 'Rua Pindaíba, 33', '11874259631', 'V2343')
librarian.borrow_books(livro, usuario)


# Adiciona novos Livros 
novos_livros = ['Livro B', 'Livro C']
librarian._add_new_books(novos_livros)

print(librarian.get_books())

librarian._remove_books(novos_livros)
print(librarian.get_books()) 
