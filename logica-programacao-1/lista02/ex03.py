def substring_str(lista):
    substrings = []

    for substring in lista:
        for palavra in lista:
            if substring != palavra and substring in palavra:
                if substring not in substrings:
                    substrings.append(substring)

    return sorted(substrings)
