import flet as ft

from database import Database
from model import Book

# Imagem padrão quando o livro não tem capa (ou a URL não carrega).
# Como o app roda com assets_dir="assets", o caminho é relativo à pasta assets.
IMG_ERR_DEF = 'img_err.jpeg'


def format_price(price: float) -> str:
    ''' 39.9 -> "R$ 39,90" '''
    return "R$ " + f"{price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def book_cover(src: str, width: int, height: int) -> ft.Image:
    ''' imagem da capa; se a URL estiver vazia ou quebrada, mostra a imagem padrão. '''
    if not src.strip():
        src = IMG_ERR_DEF
    return ft.Image(
        src=src,
        width=width,
        height=height,
        fit=ft.BoxFit.COVER,
        error_content=ft.Image(src=IMG_ERR_DEF, width=width, height=height, fit=ft.BoxFit.COVER),
    )


# ---------------------------------------------------------------------------
# TELA 1 - cadastro + lista de livros  (rota "/")
# ---------------------------------------------------------------------------
@ft.control
class BookApp(ft.Container):
    def init(self):
        self.db = Database()
        self.expand = True
        self.padding = 10
        self.title_txt = ft.TextField(label="Title", expand=True)
        self.author_txt = ft.TextField(label="Author", expand=True)
        self.desc_txt = ft.TextField(label="Description", expand=True)
        self.price_txt = ft.TextField(label="Price", expand=True, prefix="R$ ",
                                      keyboard_type=ft.KeyboardType.NUMBER)
        self.url_txt = ft.TextField(label='Book Cover Image (URL)', expand=True)
        self.output_col = ft.Column(
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            scroll=ft.ScrollMode.AUTO,
            controls=[]
        )
        save_btn = ft.IconButton(
            icon=ft.Icons.ADD,
            on_click=self.save_book
        )
        fields_col = ft.Column(
            expand=True,
            controls=[
                self.title_txt, self.author_txt,
                self.desc_txt, self.price_txt, self.url_txt]
        )
        input_row = ft.Row(
            controls=[fields_col, save_btn]
        )

        self.content = ft.Column(
            expand=True,
            controls=[input_row, ft.Divider(), self.output_col]
        )
        # carrega os livros já salvos no banco
        self.load_books()

    def load_books(self):
        self.output_col.controls.clear()
        books = self.db.fetch_all()
        for book in books:
            self.new_book_entry(book)

    def new_book_entry(self, book: Book):
        book_cover_img = book_cover(book.cover, width=100, height=150)
        book_info_col = ft.Column(
            expand=True,
            controls=[
                ft.Text(book.title, size=18, weight=ft.FontWeight.BOLD),
                ft.Text(book.author, italic=True),
                ft.Text(book.desc, max_lines=3, overflow=ft.TextOverflow.ELLIPSIS)
            ]
        )

        book_price_txt = ft.Text(format_price(book.price), size=16, weight=ft.FontWeight.BOLD)
        book_row = ft.Row(
            controls=[book_cover_img, book_info_col, book_price_txt]
        )
        card = ft.Card(
            content=ft.Container(
                content=book_row,
                padding=10,
                ink=True,
                # <click> no card -> abre a tela de detalhes desse livro
                on_click=lambda e, book_id=book.id: self.open_book(book_id),
            )
        )
        self.output_col.controls.append(card)

    def open_book(self, book_id: int):
        self.page.navigate(f"/book/{book_id}")

    def clear_fields(self):
        self.title_txt.value = ""
        self.author_txt.value = ""
        self.desc_txt.value = ""
        self.price_txt.value = ""
        self.url_txt.value = ""

    def save_book(self, e):
        # aceita "39,90" ou "39.90"
        try:
            price = float(self.price_txt.value.replace(",", "."))
            self.price_txt.error = None
        except ValueError:
            self.price_txt.error = "Digite um número, ex: 39,90"
            self.update()
            return

        title = self.title_txt.value
        author = self.author_txt.value
        desc = self.desc_txt.value
        cover = self.url_txt.value
        book = Book(title, author, desc, price, cover)
        self.db.insert(book)  # o insert preenche book.id
        self.new_book_entry(book)
        self.clear_fields()
        self.update()


# ---------------------------------------------------------------------------
# TELA 2 - detalhes de um livro  (rota "/book/<id>")
# ---------------------------------------------------------------------------
@ft.control
class BookDetail(ft.Container):
    book_id: int = 0

    def init(self):
        self.db = Database()
        self.expand = True
        self.padding = 20
        book = self.db.fetch_by_id(self.book_id)

        self.btnVoltar = ft.Button("Voltar", icon=ft.Icons.ARROW_BACK, on_click=self.on_click_btn_voltar)

        if book is None:
            self.content = ft.Row(controls=[ft.Column(
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.Text("Livro não encontrado", size=20), self.btnVoltar],
            )])
            return

        self.col = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                book_cover(book.cover, width=200, height=300),
                ft.Text(book.title, size=26, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text(f"({book.author})", size=18, italic=True, text_align=ft.TextAlign.CENTER),
                ft.Container(
                    width=500,
                    content=ft.Text(
                        spans=[
                            ft.TextSpan("Description: ", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                            ft.TextSpan(book.desc),
                        ],
                    ),
                ),
                ft.Text(format_price(book.price), size=22, weight=ft.FontWeight.BOLD),
                self.btnVoltar,
            ],
        )
        # mesmo esquema do ChangeScreen: Row + Column(expand) centraliza tudo
        self.content = ft.Row(controls=[self.col])

    def on_click_btn_voltar(self, e):
        self.page.navigate("/")
