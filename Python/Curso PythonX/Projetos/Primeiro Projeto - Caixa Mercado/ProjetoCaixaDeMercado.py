def inserirProdutos():
    dadosDaCompra = {}
    inserirDetalhes = True
    while inserirDetalhes:
        detalhes = input("Pressione A para adicionar um produto e Q para sair: ")
        if detalhes == "A":
            produto = input("Insira o produto: ")
            quantidade = int(input("Insira a quantidade: "))
            dadosDaCompra.update({produto : quantidade})
        elif detalhes == "Q":
            inserirDetalhes = False
        else:
            print("Por favor, selecione uma opção correta.")
    return dadosDaCompra

def pegarPreco(produto, quantidade):
    dadosDePreco = {
        "Biscoito" : 3,
        "Frango" : 5,
        "Ovo" : 1,
        "Peixe" : 3,
        "Refrigerante" : 2,
        "Pão" : 2,
        "Maçã" : 3,
        "Cebola" : 3
    }
    subtotal = dadosDePreco[produto] * quantidade
    print(produto + ": " + str(dadosDePreco[produto]) + "$" + " x " + str(quantidade) + " = " + str(subtotal))
    return subtotal

def pegarDesconto(valorDaConta, nivelDeMembro):
    valorOriginal = valorDaConta
    desconto = 0
    if valorDaConta >= 25:
        if nivelDeMembro == "Ouro":
            valorDaConta = valorDaConta * 0.80
            desconto = 20
        elif nivelDeMembro == "Prata":
            valorDaConta = valorDaConta * 0.90
            desconto = 10
        elif nivelDeMembro == "Bronze":
            valorDaConta = valorDaConta * 0.95
            desconto = 5
        print(str(desconto) + "% de desconto para membros de nível " +
              nivelDeMembro +
                                          " " + "no total do valor: "
+ str(valorOriginal) + "$")
    else:
        print("Sem descontos para compras abaixo de 25$")
    return valorDaConta

def criarConta(dadosDaCompra, nivelDeMembro):
    valorDaConta = 0
    for key, value in dadosDaCompra.items():
        valorDaConta += pegarPreco(key, value)
    valorDaConta = pegarDesconto(valorDaConta, nivelDeMembro)
    print("Valor total da compra: " + str(valorDaConta) + "$")

dadosDaCompra = inserirProdutos()
nivelDeMembro = input("Insira o nível de membro do cliente: ")
criarConta(dadosDaCompra, nivelDeMembro)
