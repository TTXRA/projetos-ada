def avaliacao(lista):
    resultado = ""

    for aluno in lista:
        nome = aluno["nome"]
        nota = aluno["nota"]
        faltas = aluno["faltas"]
        presenca = (60 - faltas) / 60 * 100

        if nota >= 7 and presenca >= 60:
            resultado = nome + " está aprovado(a)"
        else:
            resultado = nome + " está reprovado(a)"

    return resultado