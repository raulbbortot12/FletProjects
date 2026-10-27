import flet as ft


@ft.control
class Tela1(ft.Container):
    def init(self):
        self.txtTela1 = ft.Text(value="Tela 1", size=30, color=ft.Colors.WHITE)
        self.btnGo = ft.Button("Ir para Tela 2", on_click=self.go_to_tela2)
        self.bgcolor = ft.Colors.BLUE
        self.expand = True
        self.col = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[self.txtTela1, self.btnGo],
        )
        self.content = ft.Row(controls=[self.col])

    def go_to_tela2(self, e):
        self.page.navigate("/tela2")


@ft.control
class Tela2(ft.Container):
    def init(self):
        self.txtTela2 = ft.Text(value="Tela 2", size=30, color=ft.Colors.WHITE)
        self.btnGoBack = ft.Button("Voltar para Tela 1", on_click=self.on_click_btn_go_back)
        self.bgcolor = ft.Colors.GREEN
        self.expand = True
        self.col = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[self.txtTela2, self.btnGoBack],
        )
        self.content = ft.Row(controls=[self.col])

    def on_click_btn_go_back(self, e):
        self.page.navigate("/")


def main(page: ft.Page):
    page.title = "App"
    page.padding = 0

    def route_change_listener(e=None):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                padding=0,
                controls=[Tela1()],
                appbar=ft.AppBar(title=ft.Text("App")),
            )
        )
        if page.route == "/tela2":
            page.views.append(
                ft.View(
                    route="/tela2",
                    padding=0,
                    controls=[Tela2()],
                    appbar=ft.AppBar(title=ft.Text("App")),
                )
            )
        page.update()

    async def view_pop_listener(e):
        # Seta de "voltar" da AppBar: remove a tela de cima e volta pra anterior
        if e.view is not None:
            page.views.remove(e.view)
            await page.push_route(page.views[-1].route)

    page.on_route_change = route_change_listener
    page.on_view_pop = view_pop_listener

    # No Flet 1.x nao existe mais page.go(); chamamos o listener direto
    route_change_listener()


if __name__ == "__main__":
    ft.run(main)
