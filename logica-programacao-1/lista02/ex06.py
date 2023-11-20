def valor_final_produto(lista):
    preco = lista[0]
    estado = lista[1]
    imp = 0

    if estado in [1.0, 2.0, 3.0]:
        if estado == 1.0:
            imp = 0.07
        elif estado == 2.0:
            imp = 0.12
        elif estado == 3.0:
            imp = 0.15

        total = preco
        total += preco * imp
        total = round(total, 4)
    else:
        total = -1

    return total