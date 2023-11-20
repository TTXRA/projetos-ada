def melhores_alunos(lista):
    total_notas = 0
    total_alunos = len(lista)

    for aluno in lista:
        total_notas += aluno["nota"]

    media_turma = total_notas / total_alunos

    alunos_aprovados = []
    
    for aluno in lista:
        if aluno["nota"] >= media_turma:
            alunos_aprovados.append(aluno["nome"])

    return alunos_aprovados