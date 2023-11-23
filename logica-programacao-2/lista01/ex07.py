def removerElementosVazios(listaA):
    listaB = []

    for i in listaA:
        if i != "":
            listaB.append(i)

    return listaB