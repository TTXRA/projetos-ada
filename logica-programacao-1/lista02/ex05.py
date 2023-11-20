def soletrando_invertido_str(palavra):
    lista = list(palavra)
    listaInvertida = []

    while len(lista) > 0:
        listaInvertida.append(lista.pop())

    return listaInvertida