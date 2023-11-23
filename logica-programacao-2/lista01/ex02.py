def calculaPotencia(tuplaA):
    lista = []

    for i in range(len(tuplaA)):
        lista.append(pow(tuplaA[i], i))

    return lista