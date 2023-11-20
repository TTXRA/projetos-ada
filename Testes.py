vendas = "data, produto, quantidade, valor\n20/10/2022, ventilador, 1, 120.00\n19/20/2022, cadeira, 1, 335.55\n07/07/2022, lampada, 3, 68.90"


def produto_mais_vendido(vendas):
    lista_vendas = vendas.split("\n")
    quantidade = 0

    for linha in lista_vendas[1:]:
        item = linha.split(", ")
        if int(item[2]) > quantidade:
            quantidade = int(item[2])
            produto = item[1]

    return produto

def media_vendas(vendas):
    lista_vendas = vendas.split("\n")
    valor_lista = []

    for linha in lista_vendas[1:]:
        item = linha.split(", ")
        valor_lista.append(int(item[2])*float(item[3]))

    return round(sum(valor_lista), 2)


print(produto_mais_vendido(vendas))

min_max_temperatura([["25/11/2022", 30], ["26/11/2022", 27], ["27/11/2022", 31],["28/11/2022", 29], ["29/11/2022", 20]]), ["27/11/2022", "29/11/2022"]

