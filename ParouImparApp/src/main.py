import flet as ft

def main(page: ft.Page):
    # ----Event Listener----
    def on_click_send(e):
          value = input_text.value
          try:
            int_value = int(value)
            if (int_value % 2 == 0):
                output_txt.value += f'{int_value} é par.\n'
            else:
                output_txt.value += f'{int_value} é ímpar.\n'
          except ValueError:
            output_txt.value += f'{value} não é um número inteiro válido.\n'
          input_text.value = ''
          
    #----- Widgets -----
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
