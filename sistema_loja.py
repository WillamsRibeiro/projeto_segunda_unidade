lista_cliente = {}
mercadorias={}


def exibir():
    print('1- cadastrar cliente\n2- para cadastrar produtos\n3- editar \n4- relatorio\n5- relatorio produtos')

def opcoes_do_programa():
    exibir()
    opcao=int(input())

    while opcao !=0 :

        if opcao == 1:
            nome = input("nome do cliente:  ")
            telefone = int(input('digite o numero: '))
            endereco = input ('rua/numero/cidade/bairro: ')
            lista_cliente[nome]= {'nome':nome , 'contato': telefone, 'local': endereco}
            print(f"cliente: {lista_cliente[nome]['nome']} | telefone: {lista_cliente[nome]['contato']} | endereço: {lista_cliente[nome]['local']}")
            input('pressione uma tecla para retornar')


        elif opcao == 2:
            cod= input("codigo: ")
            nome = input('digite o produto: ')
            categoria = input('tipo do produto: ')
            linha = input('digite a linha do produto: ')
            qtd = int(input('digite a quantidade do produto: '))
            val=input('digite o mês que vence o produto: ')
            ano= int(input('Ano de vencimento: '))
            preco= float(input('preço de compra: '))
            preco_venda = float(input('preço de venda: '))

            mercadorias[cod] = {'cod': cod, 'nome': nome, 'quantidade': qtd, 'catg': categoria, 'segmento': linha,
                                     'mês': val, 'tempo': ano, 'compra': preco, 'venda': preco_venda}


            print(f'''produto cod: {mercadorias[cod]["cod"]} |nome: {mercadorias[cod]["nome"]} |categoria: {mercadorias[cod]["catg"]} |linha: {mercadorias[cod]["segmento"]}| quantidade: {mercadorias[cod]["quantidade"]} 
            | vecimento: {mercadorias[cod]["mês"]} |ano: {mercadorias[cod]["tempo"]} |investimento: {mercadorias[cod]["compra"]} |preço de venda: {mercadorias[cod]["venda"]}''')

            input('pressione uma tecla para retornar')
        elif opcao == 3:
            pass



        elif opcao ==4:
            relatorio()
            print('1- cadastrar cliente\n2- para cadastrar produtos\n3- relatorio de vendas\n4- editar cliente:')
            int(input(''))

        elif opcao ==5:
           pass

    else:
        pass
        opcoes_do_programa()
def relatorio():

    nome_cliente = input('digite o nome do cliente\n ')

    if nome_cliente in lista_cliente:
            print(f' nome: {lista_cliente[nome_cliente]["nome"]}| telefone::{lista_cliente[nome_cliente]["contato"]} | endereço:{lista_cliente[nome_cliente]["local"]}')
            input('pressione uma tecla para retornar')
    else:
            print('cliente não cadastrado')
            input('pressione uma tecla para retornar')
def editar():
   pass
def produtos():
    pass
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
