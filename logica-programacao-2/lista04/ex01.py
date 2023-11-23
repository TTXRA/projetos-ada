def verifica_extensao(path):
    ext_validas = ['jpg', 'jpeg', 'png']
    ext = path.split('.')[-1]

    if ext in ext_validas:
        return f"A extensão '{ext}' é válida."
    else:
        raise Exception("Formato inválido")