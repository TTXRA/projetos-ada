def numero_unico(lista):
    num = 0

    for i in lista:
        if lista.count(i) == 1:
            num = i

    return num