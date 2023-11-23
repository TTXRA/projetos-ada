def par_e_impar(lista):
    pares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1

    impares = len(lista) - pares

    if pares == 1:
        resultadoPares = "1 par"
    else:
        resultadoPares = f"{pares} pares"

    if impares == 1:
        resultadoImpares = "1 ímpar"
    else:
        resultadoImpares = f"{impares} ímpares"

    return f"{resultadoPares}, {resultadoImpares}"