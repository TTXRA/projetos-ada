def elementos_repetidos(lista):
    tmp_rep = []

    for i in lista:
        if lista.count(i) > 1:
            tmp_rep.append(i)

    if len(tmp_rep) > 0:
        return f"Sim, existem {len(tmp_rep)} dias com temperatura média repetida."
    else:
        return "Não, não existem dias com temperatura média repetida."