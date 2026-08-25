import flet as ft   

# lista de emojis que irão aparecer no app
# essa lista pode ser ampliada, o aplicativo irá lidar com isso
EMOJIS= ["😀", "😂", "😎", "😍", "🤔", "😢", "😡", "👍", "👎", "🎉", "🌟"]
# IDX controla o índice da lista de emojis. Sempre estará
# atualizado com o índice do emoji que está sendo exibido
# na tela 
IDX = 0

#a função main recebe o objeto página, que carrega todos os elementos gráficos (controls)
#Page é criado pelo framework flet durante a execução.
def main(page: ft.Page):
    #----- configurações da página editar a título da janela/aba do navegador/nome do app
    page.title = 'EmojiApp'
    #alinha verticalemente o elemento (control) que foi inserido na página 
    #ft.MainAxisAlignment.CENTER é uma constante do framework flet que indica que o elemento deve ser centralizado verticalmente
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #------meus elementos (controls)
    #ft.Text é um elemento de texto do framework flet, que recebe como parâmetro o valor do texto que será exibido na tela
    input = ft.Text(value=EMOJIS[0],size=100)

    #----- função aninhada na main
    #Esta é a função que é executada ao clicar em "btn".
    #A função aninhada à main para que ela consiga acessar as variáveis declaradas na função main (ex. variável input)
    #A função acresce o valor de IDX para mostrar o próximo emoji da lista
    # O parâmentro "e" da função carrega informações sobre o evento executado, é possível acessar a partir de "e" o elemento que sofreu o evento
    def refresh_click(c):
        global IDX 
        #Incrmento circular:
        #   * Acresce IDX em 1
        #   * Se IDX > tamanho da lista de emojis, então IDX volta a ser 0
        #     OBS: IDX nunca passa do maior índice da lista
        #      IDX = 0,1,2,3,4,0,1,2,3,4,0....
        IDX = (IDX + 1) % len(EMOJIS)
        input.value = EMOJIS[IDX]

    btn = ft.ElevatedButton("Next Emoji", on_click=refresh_click)
    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[input, btn]
    )




    page.add(row)

if __name__ == "__main__":
    ft.run(main)