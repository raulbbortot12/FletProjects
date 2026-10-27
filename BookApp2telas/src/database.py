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

INSERT_BOOK_QUERY = '''INSERT INTO books (title, author, desc, price, cover) VALUES (?, ?, ?, ?, ?)'''

FETCH_BOOKS_QUERY = '''SELECT id, title, author, desc, price, cover FROM books;'''

FETCH_BOOK_BY_ID_QUERY = '''SELECT id, title, author, desc, price, cover FROM books WHERE id = ?;'''


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
            # Ensure the `cover` column exists (migrate older DBs)
            cur = conn.execute("PRAGMA table_info(books);")
            cols = [row[1] for row in cur.fetchall()]
            if 'cover' not in cols:
                conn.execute("ALTER TABLE books ADD COLUMN cover TEXT;")
    def insert(self, book:Book):
        ''' insere um livro no banco de dados. '''
        with self.__connect() as conn:
            cur = conn.execute(
                INSERT_BOOK_QUERY, (book.title, book.author, book.desc, book.price, book.cover)
            )
            # guarda o id gerado pelo banco, para poder abrir a tela de detalhes depois
            book.id = cur.lastrowid
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
               ret.append(self.__row_to_book(row))
        return ret

    def fetch_by_id(self, book_id: int) -> Book | None:
        ''' retorna o livro com o id informado, ou None se ele não existir. '''
        with self.__connect() as conn:
            cur = conn.cursor()
            cur.execute(FETCH_BOOK_BY_ID_QUERY, (book_id,))
            row = cur.fetchone()
        if row is None:
            return None
        return self.__row_to_book(row)

    def __row_to_book(self, row) -> Book:
        ''' transforma uma linha (tupla) do banco em um objeto Book. '''
        return Book(
            id=int(row[0]),
            title=str(row[1]),
            author=str(row[2]),
            desc=str(row[3]),
            price=float(row[4]),
            cover=str(row[5] or '')
        )