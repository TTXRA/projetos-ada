def remove_espacos(listaStrings):
    return [' '.join(palavra.strip().split()) for palavra in listaStrings]