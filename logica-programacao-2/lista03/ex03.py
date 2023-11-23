def produto_mais_vendido(vendas):
    lista_vendas = vendas.split("\n")
    quantidade = 0

    for linha in lista_vendas[1:]:
        item = linha.split(", ")
        if int(item[2]) > quantidade:
            quantidade = int(item[2])
            produto = item[1]

    return produto