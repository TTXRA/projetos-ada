def calcula_valor_entrada(lista):
    dia = lista[0]
    preco = lista[1]
    musica = lista[2]

    entrada = preco

    if dia in [1.0, 2.0, 4.0]:
        entrada -= 0.25 * preco

    if musica == 1.0:
        entrada += 0.15 * entrada

    return round(entrada, 3)