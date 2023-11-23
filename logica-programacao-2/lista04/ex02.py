def verifica_numero(x1):
    try:
        return int(x1)
    except ValueError:
        raise TypeError("Apenas números inteiros permitidos. Digite novamente")