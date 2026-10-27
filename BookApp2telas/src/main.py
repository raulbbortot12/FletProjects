import flet as ft
from view import BookApp, BookDetail


def main(page: ft.Page):
    page.title = "Book App"
    page.padding = 0

    def route_change_listener(e=None):
        page.views.clear()

        # Tela 1 (sempre fica embaixo na pilha)
        page.views.append(
            ft.View(
                route="/",
                padding=0,
                controls=[BookApp()],
                appbar=ft.AppBar(title=ft.Text("BookApp"), center_title=True),
            )
        )

        # Tela 2: rota no formato "/book/<id>"
        if page.route.startswith("/book/"):
            book_id = page.route.split("/")[-1]
            if book_id.isdigit():
                page.views.append(
                    ft.View(
                        route=page.route,
                        padding=0,
                        controls=[BookDetail(book_id=int(book_id))],
                        appbar=ft.AppBar(title=ft.Text("BookApp"), center_title=True),
                    )
                )
        page.update()

    async def view_pop_listener(e):
        # Seta "<-" da AppBar: remove a tela de cima e volta pra anterior
        if e.view is not None:
            page.views.remove(e.view)
            await page.push_route(page.views[-1].route)

    page.on_route_change = route_change_listener
    page.on_view_pop = view_pop_listener

    # No Flet 1.x não existe page.go(); chamamos o listener direto
    route_change_listener()


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
