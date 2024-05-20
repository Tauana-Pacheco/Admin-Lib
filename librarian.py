from datetime import datetime
from borrow import Borrow
from user import User
from books import Book

class Librarian:
  def __init__(self, id_librarian):
    self.id_librarian = id_librarian

  # Empresta livro
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
  
  # Devolve Livro
  def return_books(self, emprestimo):
    emprestimo.data_devolucao = datetime.now().strftime("%Y-%m-%d")
    emprestimo.livro.disponivel = True
    print(f"Livro '{emprestimo.livro.titulo}' devolvido por {emprestimo.usuario.nome} em {emprestimo.data_devolucao}.")  

  # Adiciona novos Livros 
  def add_new_books(self, new_books):
    self.books.append(new_books)
      
  # Remove Livros
  def remove_books(self, books):
    self.books.remove(books)
  
#  id, isbn, title, author, year_of_publication, num_of_editions, num_of_copies, num_of_pages
livro = Book('978-3-16-148410-0', "O Senhor dos Anéis", "J.R.R. Tolkien", "123456789", 10, 20, 1000)
usuario = User("Alice", "senha123", 25, "alice@example.com", "123 Main Street", "555-1234", "12345", True)
# bibliotecario = Librarian("Maria")

librarian = Librarian("Lucas")
librarian.borrow_books(livro, usuario)

  

