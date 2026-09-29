import os 
import sqlite3
from model import Book

DB_PATH = os.path.join(os.environ['FLET_APP_STORAGE_DATA'], "bookapp.db")

# os.path.join concatena caminhos com o separador do sistema
#i.e. "/" no Linux e "\" no Windows
BOOKAPP_SQL_PATH = os.path.join(
    # nome do diretório em que o arquivo database.py está.
    # ex. /home/aluno/python-intro/FletProjects/BookApp/src
    os.path.dirname(os.path.abspath(__file__)),
    "sql",
    "bookapp.sql"
)

INSERT_BOOK_QUERY = '''INSERT INTO books (title, author, desc, price) VALUES (?, ?, ?, ?)'''

FETCH_BOOKS_QUERY = '''SELECT title, author, desc, price FROM books;'''


class Database(object):
    def __init__(self):
        self.create_tables()
    def __connect(self)->sqlite3.Connection:
        ''' abre o arquivo squilite para colsulta/modificação. Se o arquivo não existir, ele será criado.'''
        return sqlite3.connect(DB_PATH)
    def create_tables(self):  # Remova os "__" do começo
        ''' cria as tabelas do banco de dados, caso elas não existam.
          * abre conexão "conn" com o banco sqlite
          * abre o arquivo "bookapp.sql" em "sqlf"
          * cria tabelas a partir da leitura do script
          * fecha "conn" e "sqlf" automaticamente ao sair do bloco with
        '''

        with self.__connect() as conn:
            with open(BOOKAPP_SQL_PATH, "r", encoding='utf-8') as sqlf:
                sql_script = sqlf.read()
                conn.executescript(sql_script)
    def insert(self, book:Book):
        ''' insere um livro no banco de dados. '''
        with self.__connect() as conn:
            conn.execute(
                INSERT_BOOK_QUERY, (book.title, book.author, book.desc, book.price)
            )
    def fetch_all(self) -> list[Book]:
        ''' retorna uma lista de livros do banco de dados. '''

        ret = []
        with self.__connect() as conn:
            cur = conn.cursor()
            cur.execute(FETCH_BOOKS_QUERY)
            #cada valor de rows corresponde a uma tupla contendo o s valores do registro de livro
            rows = cur.fetchall()
            # para cada linha de resultado, faça:
            for row in rows:
               book = Book(
                    title=str(row[0]),
                    author=str(row[1]),
                    desc=str(row[2]),
                    price=float(row[3])
               )
               ret.append(book)
        return ret