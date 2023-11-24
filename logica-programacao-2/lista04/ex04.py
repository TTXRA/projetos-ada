def divide_dois_numeros(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero não é permitida.")