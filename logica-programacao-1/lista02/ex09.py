def par_e_impar(lista):
    pares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1

    impares = len(lista) - pares

    if pares > 1:
        if impares > 1:
            resultado = f"{pares} pares, {impares} ímpares"
        else:
            resultado = f"{pares} pares, {impares} ímpar"
    elif impares > 1:
        if pares > 1:
            resultado = f"{pares} pares, {impares} ímpares"
        else:
            resultado = f"{pares} par, {impares} ímpares"

    return resultado