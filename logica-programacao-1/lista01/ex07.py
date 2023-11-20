def custo_compra(qtd_frutas):
    if qtd_frutas > 10:
        valor = qtd_frutas * 1.25
    else:
        valor = qtd_frutas * 1.45

    return round(valor, 2)