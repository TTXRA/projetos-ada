def ordena_lista(listaA):
    listaB = []

    while len(listaA):
        var = max(listaA)
        listaB.append(var)
        listaA.remove(var)

    return listaB