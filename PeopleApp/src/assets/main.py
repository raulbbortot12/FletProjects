import flet as ft


def main(page: ft.Page):

    page.title = "Cadastro de Pessoas"
    page.padding = 30

    nome = ft.TextField(
        hint_text="Nome",
        prefix_icon=ft.Icons.PERSON,
        width=500,
    )

    idade = ft.TextField(
        hint_text="Idade",
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        width=500,
    )

    email = ft.TextField(
        hint_text="E-mail",
        prefix_icon=ft.Icons.EMAIL,
        width=500,
    )

    lista = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
    )

    def adicionar(e):

        if nome.value and idade.value and email.value:

            lista.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            f"{nome.value}, {idade.value}",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            email.value,
                            size=17,
                        ),
                    ]),
                    padding=15,
                    border=ft.Border(left=ft.BorderSide(1, "#DDDDDD"), right=ft.BorderSide(1, "#DDDDDD"), top=ft.BorderSide(1, "#DDDDDD"), bottom=ft.BorderSide(1, "#DDDDDD")),
                    border_radius=10,
                )
            )

            nome.value = ""
            idade.value = ""
            email.value = ""

            page.update()

    botao = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color="white",
        bgcolor="#4285F4",
        icon_size=35,
        on_click=adicionar,
    )

    page.add(

        ft.Row([
            ft.Column([
                nome,
                idade,
                email,
            ]),
            botao,
        ]),

        ft.Divider(),

        ft.Container(
            content=lista,
            height=400,
        ),
    )


ft.run(main)

