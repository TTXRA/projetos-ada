def mediaAlunosParaDicionario(listaAlunos):
    return {aluno:float(media) for aluno, media in zip(listaAlunos[0],listaAlunos[1])}