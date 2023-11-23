def mediaPrecoCelular(dictCelulares):
    media = sum(dictCelulares['valor'])/len(dictCelulares['valor'])
    menor = min(dictCelulares['valor'])
    maior = max(dictCelulares['valor'])

    return [media, menor, maior]