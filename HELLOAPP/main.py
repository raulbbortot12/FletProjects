import flet as ft

def main(page: ft.Page):
    page.title = 'HelloApp'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    text = ft.Text(value="Hello, World!")

    text = ft.Text(
        value="Hello, World!",
        text_align=ft.TextAlign.CENTER,
        width=999
    )



    page.add(text)
    pass

if __name__ == "__main__":
    ft.app(target=main) 