def ordena(lista):
    listaOrdenada = []

    while len(lista) > 0:
        menor = min(lista)
        listaOrdenada.append(menor)
        lista.remove(menor)

    return listaOrdenada