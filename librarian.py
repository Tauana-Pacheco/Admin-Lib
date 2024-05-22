from db import create_connection, close_connection
from datetime import datetime
from borrow import Borrow
from user import User
from books import Book
from employee import Employee

class Librarian(Employee):
  def __init__(self, name, _password, _age, _email, _address, _contact, id_librarian):
    super().__init__(name, _password, _age, _email, _address, _contact, "Biliotecaria")
    self.id_librarian = id_librarian
    self.books = []

  def get_books(self):
     return self.books

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

  # Adiciona novos Livros 
  def _add_new_books(self, books):
      for book in books:
          self.books.append(book)
      
  # Remove Livros
  def _remove_books(self, books):
     for book in books:
          self.books.remove(book)
      
  #  v2_ add busca