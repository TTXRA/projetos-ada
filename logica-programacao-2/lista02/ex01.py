def dicionarioQuadrados(listaA):
    dicio = {}

    for i in listaA:
        dicio.update({i: (i**2)})

    return dicio