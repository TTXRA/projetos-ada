def calcula_custos_carro(lista):
    precoFinal = lista[0]
    custoDistribuidor = lista[1]
    valorImpostos = lista[2]

    percDistribuidor = (custoDistribuidor / precoFinal) * 100
    percImpostos = (valorImpostos / precoFinal) * 100

    percentuais = [round(percDistribuidor, 2), round(percImpostos, 2)]

    return percentuais