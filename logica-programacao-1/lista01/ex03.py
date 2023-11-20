def primeiro_caractere_unico(palavra):
    letras_lidas = []
    letras_repetidas = []

    for letra in palavra:
        if letra not in letras_lidas:
            letras_lidas.append(letra)
        else:
            letras_repetidas.append(letra)

    cont = -1

    for letra in palavra:
        cont += 1
        if letra not in letras_repetidas:
            break

    if cont == len(palavra) - 1:
        cont = -1

    return cont