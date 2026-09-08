import flet as ft


def eh_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    return True


def main(page: ft.Page):
    page.title = "PrimoApp"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        "Verificador de Número Primo",
        size=25,
        weight=ft.FontWeight.BOLD
    )

    entrada = ft.TextField(
        label="Digite um número inteiro",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    resultado = ft.Text(size=20)

    def verificar(e):
        resultado.value = ""

        try:
            numero = int(entrada.value)

            if eh_primo(numero):
                resultado.value = f"{numero} é um número primo!"
            else:
                resultado.value = f"{numero} não é um número primo!"

        except (ValueError, TypeError):
            resultado.value = "Digite um número inteiro válido."

        page.update()

    botao = ft.ElevatedButton(
        "Verificar",
        on_click=verificar
    )

    page.add(
        titulo,
        entrada,
        botao,
        resultado
    )


if __name__ == "__main__":
    ft.app(target=main)
