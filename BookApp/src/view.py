import flet as ft

from database import Database
from model import Book

IMG_ERR_DEF = 'assets/img_err.png'
 
@ft.control
class BookApp(ft.Container):
    def init(self):
       self.db = Database()
       self.expand = True
       self.title_txt = ft.TextField( label="Title", expand=True)
       self.author_txt = ft.TextField( label="Author", expand=True)
       self.desc_txt = ft.TextField( label="Description", expand=True)
       self.price_txt = ft.TextField( label="Price", expand=True)
       self.url_txt = ft.TextField( label='Book Cover Image (URL)', expand=True)
       self.output_col = ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            scroll=ft.ScrollMode.AUTO,
            controls=[]            
       )
       save_btn = ft.IconButton(
            icon = ft.Icons.ADD,
            on_click=self.save_book
       )
       fields_col = ft.Column(
           expand=True,
           controls=[
               self.title_txt,self.author_txt,
               self.desc_txt,self.price_txt, self.url_txt]
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
        if not book.cover.strip():
            book.cover = IMG_ERR_DEF
        
        book_cover_img = ft.Image(
            src=book.cover,
            width=100,
            height=150
        )
        book_info_col = ft.Column(
           controls=[
               ft.Text(book.title),
               ft.Text(book.author),
               ft.Text(book.desc)
              ]
        )

        book_price_txt = ft.Text(str(book.price))
        book_row = ft.Row(
            controls=[book_cover_img, book_info_col, book_price_txt]
        )
        card = ft.Card( 
            content=book_row
        )
        self.output_col.controls.append(card)
        self.update()
    def clear_fields(self):
        self.title_txt.value = ""
        self.author_txt.value = ""
        self.desc_txt.value = ""
        self.price_txt.value = ""
        self.url_txt.value = ""
        self.update()

    def save_book(self,e):
        title = self.title_txt.value
        author = self.author_txt.value
        desc = self.desc_txt.value
        price = float(self.price_txt.value)
        cover = self.url_txt.value
        book = Book(title, author, desc, price, cover)
        self.new_book_entry(book)
        self.db.insert(book)
        self.clear_fields()
