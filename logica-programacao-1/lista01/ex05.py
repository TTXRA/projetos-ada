def media_aproveitamento(lista):
    n1 = lista[0]
    n2 = lista[1]
    n3 = lista[2]
    medEx = lista[3]

    media = (n1 + n2*2 + n3*3 + medEx)/7

    if media >= 9.0:
        conceito = "A"
    elif 9 > media >= 7.5:
        conceito = "B"
    elif 7.5 > media >= 6:
        conceito = "C"
    else:
        conceito = "D"

    return conceito