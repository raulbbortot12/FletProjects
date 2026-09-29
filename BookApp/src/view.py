import flet as ft 

from database import Database
from model import Book

@ft.control
class BookApp(ft.Container):
    def init(self):
       self.db = Database()
       self.title_txt = ft.TextField( label="Title")
       self.author_txt = ft.TextField( label="Author")
       self.desc_txt = ft.TextField( label="Description")
       self.price_txt = ft.TextField( label="Price")
       self.output_col = ft.Column()
       save_btn = ft.IconButton(
            icon = ft.Icons.ADD,
            on_click=self.save_book
       )
       fields_col = ft.Column(
           controls=[
               self.title_txt,self.author_txt,
               self.desc_txt,self.price_txt]
       )
       input_row = ft.Row(
                  controls=[fields_col, save_btn]
       )
       
       self.content = ft.Column(
           controls=[input_row, self.output_col]
       )
       
    def load_books(self):
        self.output_col.controls.clear()
        books = self.db.fetch_all()
        for book in books:
            self.new_book_entry(book)

    def new_book_entry(self, book: Book):
        book_info_col = ft.Column(
           controls=[
               ft.Text(book.title),
               ft.Text(book.author),
               ft.Text(book.desc)
              ]
        )

        book_price_txt = ft.Text(book.price)
        book_row = ft.Row(
            controls=[book_info_col, book_price_txt]
        ) 
        self.output_col.controls.append(book_row)
        self.update()

    def save_book(self,e):
        title = self.title_txt.value
        author = self.author_txt.value
        desc = self.desc_txt.value
        price = float(self.price_txt.value)
        book = Book(title, author, desc, price)
        self.new_book_entry(book)
        self.db.insert(book)
