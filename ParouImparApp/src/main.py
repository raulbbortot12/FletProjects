import flet as ft

def main(page: ft.Page):
    # ----Event Listener----
    def close_dialog(e):   
        page.pop_dialog()
        page.update()

    def on_click_send(e):
        value = input_text.value
        try:
            int_value = int(value)
            output_txt.value = ft.Text(value = '')  
            if (int_value % 2 == 0):
                output_txt.value += f'{int_value} é par.\n'
            else:
                output_txt.value += f'{int_value} é ímpar.\n'
                output_col.controls.append(output_txt)  
        except ValueError:
            if(value.strip() == ''):
                dialog.content = ft.Text('O campo está vazio.')
            else:
                dialog.content = ft.Text(f'{value} não é um número inteiro válido.')
            page.show_dialog(dialog)
        input_text.value = ''
        page.update()

    #----- Widgets -----
    dialog = ft.AlertDialog(
        title=ft.Text("Erro"),
        content=ft.Text("Mensagem de erro"),
        actions=[ft.TextButton("fechar", on_click=close_dialog)],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    input_text = ft.TextField(
        expand=True,
        hint_text='Digite um número inteiro...'
    )
    input_btn = ft.IconButton(
        icon=ft.Icons.SEND,
        on_click=on_click_send
    )
    output_txt = ft.Text(value = '')

    #----- Layout -----
    input_row = ft.Row( 
        controls=[input_text, input_btn]
    )
    output_col = ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        scroll= ft.ScrollMode.AUTO,
        controls=[output_txt]
    )
    main_col = ft.Column(
        expand=True,
        controls=[input_row, output_col]
    )
    #_---- Página -----
    page.title = "ParOuÍmparApp"
    page.add(main_col)

    if __name__ == "__main__":
        ft.run(main)
