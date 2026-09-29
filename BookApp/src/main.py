import flet as ft
from view import BookApp

def main(page: ft.Page):
    page.title = "Book App"
    book_app = BookApp()
    page.add(book_app)
    book_app.load_books()

if __name__ == "__main__":
    ft.run(main)
