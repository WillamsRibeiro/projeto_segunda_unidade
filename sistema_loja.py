banco_de_dados = {}


def exibir():
    print('1- cadastrar produtos\n2- editar preço \n3- relatorio\n4- excluir')

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
            print(f" código do produto:  nome: {banco_de_dados[cod]['nome']} | categoria: {banco_de_dados[cod]['categoria']} | vencimento: {banco_de_dados[cod]['val']} | ano {banco_de_dados[cod]['ano']} | faturamento {banco_de_dados[cod]['venda']}")
            input('pressione uma tecla para retornar')
            opcoes_do_programa()


        elif opcao == 2:
            editar()
            input('pressione uma tecla para retornar ')
            opcoes_do_programa()


        elif opcao ==3:
            print()
            relatorio()

            int(input())
            opcoes_do_programa()

        elif opcao ==4:
            excluir()
            input('pressione uma tecla para retornar ')
            opcoes_do_programa()


    else:

        opcoes_do_programa()

def relatorio():


    produto = input('digite o código do produto\n ')

    if produto in banco_de_dados:
            print(banco_de_dados[produto])
            input('pressione uma tecla para retornar ')
            opcoes_do_programa()
    else:
        print('produto não cadastrado')
        input('pressione uma tecla para retornar ')
        opcoes_do_programa()

def editar():
    print(banco_de_dados)
    cod=input('codigo do produto ')
    if cod in banco_de_dados:
        banco_de_dados['venda'] = input('digite o novo preço')
        print(f'{banco_de_dados}')

def excluir():
    print (banco_de_dados)
    cod = input('digite o código do produto que deseja excluir\n')
    print(f' tem certeza que deseja excluir o produto? {cod}')
    if cod in banco_de_dados:
        del banco_de_dados[cod]
        print(f'produto {cod} excluído com sucesso!')
        print(f"banco de dados atualizado {banco_de_dados}")
    else:
        print('produto não encontrado')
    print('banco de dados atualizado ',banco_de_dados)
    opcoes_do_programa()

def main():
    opcoes_do_programa()
    relatorio()
    editar()
    excluir()
if __name__ == '__main__':
    main()
