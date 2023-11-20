def substring_str(lista):
    substrings = []

    for substring in lista:
        for palavra in lista:
            if substring != palavra and substring in palavra:
                substrings.append(substring)
                break

    substringsUnicas = list(set(substrings))
    substringsOrdenadas = sorted(substringsUnicas, key=lista.index)

    return substringsOrdenadas
