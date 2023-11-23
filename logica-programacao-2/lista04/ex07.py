def divide_dois_numeros(x,y):
    try:
        if x is None or y is None:
            raise ValueError("Ambos os argumentos devem ser fornecidos.")

        resultado = x / y
        return resultado
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    except Exception as e:
        raise e