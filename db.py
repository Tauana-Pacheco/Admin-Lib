import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        connection = sqlite3.connect('library.db')
        print("Conectado ao SQLite com sucesso")
        return connection
    except Error as e:
        print(f"Erro ao conectar ao SQLite: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Conexão ao SQLite fechada")

def create_tables():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL, 
            id_user INTEGER NOT NULL,
            contact INTEGER NOT NULL,
            ativo TEXT NOT NULL                               
        );
        ''')    
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year_of_publication INTEGER NOT NULL, 
            num_of_editions INTEGER NOT NULL, 
            num_of_copies INTEGER NOT NULL, 
            num_of_pages INTEGER NOT NULL,                                               
            available BOOLEAN DEFAULT TRUE,
            type TEXT NOT NULL CHECK (type IN ('PhysicalBook', 'DigitalBook'))       
        );
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS PhysicalBook (
            id INTEGER PRIMARY KEY,
            cover_type TEXT NOT NULL,
            weight REAL NOT NULL,
            FOREIGN KEY (id) REFERENCES Book(id)
        );
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS DigitalBook (
            id INTEGER PRIMARY KEY,
            file_size TEXT NOT NULL,
            format TEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES Book(id)
            );
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Borrow (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_book INTEGER,
            id_user INTEGER,
            status TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT,
            FOREIGN KEY (id_book) REFERENCES Book(id),
            FOREIGN KEY (id_user) REFERENCES User(id)
        );
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            type TEXT NOT NULL CHECK (type IN ('Adm', 'Librarian'))
        );
        ''')
        connection.commit()
        cursor.close()
        close_connection(connection)
        print("Tabelas criadas com sucesso.")

def drop_table(table_name):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            connection.commit()
            cursor.close()
            print(f"Tabela {table_name} deletada com sucesso.")
        except Error as e:
            print(f"Erro ao deletar a tabela {table_name}: {e}")
        finally:
            close_connection(connection)

def delete_table(table_name):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM {table_name}")
            connection.commit()
            cursor.close()
            print(f"Tabela {table_name} deletada com sucesso.")
        except Error as e:
            print(f"Erro ao deletar a tabela {table_name}: {e}")
        finally:
            close_connection(connection)



#create_tables()
# drop_table('Book')
# drop_table('PhysicalBook')
# drop_table('DigitalBook')