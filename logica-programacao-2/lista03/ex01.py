def media_vendas(vendas):
    lista_vendas = vendas.split("\n")
    valor_lista = []

    for linha in lista_vendas[1:]:
        item = linha.split(", ")
        valor_lista.append(int(item[2])*float(item[3]))

    return round(sum(valor_lista), 2)