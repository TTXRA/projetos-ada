def adicionarElemento(listaA):
    if len(listaA) % 2 == 0:
        listaA.insert((len(listaA) // 2), 42)
    else:
        listaA.insert((len(listaA) // 2) + 1, 42)

    return listaA