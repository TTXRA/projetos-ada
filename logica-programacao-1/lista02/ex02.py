def soma_algarismos(numero):
    valor = 0

    if numero <= 0:
        valor = -1
    else:
        while numero > 0:
            digito = numero % 10
            valor += digito
            numero //= 10

    return valor