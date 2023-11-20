def indicador_triangulo(lista):
    a, b, c = sorted(lista)
    cond = 'Sim'

    if a >= (b + c):
        cond = 'Não'
    elif b >= (a + c):
        cond = 'Não'
    elif c >= (a + b):
        cond = 'Não'

    return cond