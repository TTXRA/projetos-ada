def calculo_salario_com_comissao(lista):
    numCarros = lista[0]
    totalVendas = lista[1]
    salFixo = lista[2]
    valFixo = lista[3]

    salario = (numCarros*valFixo) + (0.05*totalVendas) + salFixo

    return round(salario, 2)