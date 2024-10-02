banco_de_dados = {}



def exibir():
    print('1- cadastrar produtos\n2- editar \n3- relatorio\n4- excluir')

def opcoes_do_programa():
    exibir()
    opcao=int(input(""))

    while opcao !=0 :

        if opcao == 1:
            cod = input('digite o código do produto:  ')
            cosmetico = (input('digite o nome: '))
            tipo= input ('categoria do produto: ')
            validade = input('nome do  mês de vencimento: ')
            tempo = input('ano de vencimento: ')
            preco = float(input('digite o preço do produto: '))
            banco_de_dados[cod]= {'cod':cod , 'nome':cosmetico , 'categoria': tipo, 'val': validade, 'ano': tempo, 'venda': preco}
            print(f" código do produto: {banco_de_dados[cod]['cod']} | nome: {banco_de_dados[cod]['nome']} | categoria: {banco_de_dados[cod]['categoria']} | vencimento: {banco_de_dados[cod]['val']} | ano {banco_de_dados[cod]['ano']} faturamento{banco_de_dados[cod]['venda']}")
            input('pressione uma tecla para retornar')
            opcoes_do_programa()


        elif opcao == 2:
            pass



        elif opcao ==3:
            relatorio()
            print('1- cadastrar cliente\n2- para cadastrar produtos\n3- relatorio de vendas\n4- editar cliente:')
            int(input(''))

        elif opcao ==4:
            produtos()

    else:
        pass
        opcoes_do_programa()
def relatorio():

    produto = input('digite o nome do produto\n ')

    if produto in banco_de_dados.values():
        print(banco_de_dados[produto])
        input('pressione uma tecla para retornar')
    else:
        print('produto não cadastrado')
        input('pressione uma tecla para retornar')

def editar():
   pass
def produtos():
    nome_do_produto = input('digite o nome do produto ')

    if nome_do_produto in mercadorias:
        print(f' nome: {mercadorias[nome_do_produto]["nome"] }')
    else:
        print('cliente não cadastrado')
        input('pressione uma tecla para retornar')


def excluir():
    item = input('digite o nome do item que deseja excluir: ')
    mercadorias[nome]= item
    if item in mercadorias:
        del mercadorias[item]
        print('produto excluído com sucesso')











def main():

    opcoes_do_programa()
    relatorio()
    produtos()
    editar()
    excluir()
if __name__ == '__main__':
    main()
