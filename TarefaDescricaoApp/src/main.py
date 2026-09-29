import flet as ft


def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.padding = 30

    campo_tarefa = ft.TextField(
        label="Descrição da tarefa",
        hint_text="Digite uma tarefa...",
        expand=True,
    )

    lista_tarefas = ft.Column(spacing=10)


    def adicionar_tarefa(e):
        texto = campo_tarefa.value.strip()

        if not texto:
            return

        texto_tarefa = ft.Text(texto)

        checkbox = ft.Checkbox()

        prioridade = ft.Text(
            "Prioridade: Baixa",
            color=ft.Colors.GREEN,
        )

        def concluir_tarefa(e):
            if checkbox.value:
                texto_tarefa.style = ft.TextStyle(
                    decoration=ft.TextDecoration.LINE_THROUGH
                )
            else:
                texto_tarefa.style = ft.TextStyle(
                    decoration=ft.TextDecoration.NONE
                )

            page.update()

        checkbox.on_change = concluir_tarefa


        def escolher_prioridade(e):
            prioridade.value = e.control.value

            if e.control.value == "Prioridade: Baixa":
                prioridade.color = ft.Colors.GREEN

            elif e.control.value == "Prioridade: Média":
                prioridade.color = ft.Colors.ORANGE

            elif e.control.value == "Prioridade: Alta":
                prioridade.color = ft.Colors.RED

            page.update()


        menu_prioridade = ft.Dropdown(
            label="Prioridade",
            width=150,
            value="Prioridade: Baixa",
            options=[
                ft.DropdownOption(
                    key="Prioridade: Baixa",
                    text="Baixa",
                ),
                ft.DropdownOption(
                    key="Prioridade: Média",
                    text="Média",
                ),
                ft.DropdownOption(
                    key="Prioridade: Alta",
                    text="Alta",
                ),
            ],
            on_select=escolher_prioridade,
        )


        tarefa = ft.Row(
            controls=[
                checkbox,
                texto_tarefa,
                prioridade,
                menu_prioridade,
            ],
            alignment=ft.MainAxisAlignment.START,
        )

        lista_tarefas.controls.append(tarefa)

        campo_tarefa.value = ""
        campo_tarefa.focus()

        page.update()


    botao_adicionar = ft.Button(
        content="Adicionar tarefa",
        on_click=adicionar_tarefa,
    )

    page.add(
        ft.Text(
            "Lista de Tarefas",
            size=30,
            weight=ft.FontWeight.BOLD,
        ),

        ft.Row(
            controls=[
                campo_tarefa,
                botao_adicionar,
            ],
            alignment=ft.MainAxisAlignment.START,
        ),

        ft.Divider(),

        lista_tarefas,
    )


ft.run(main)
