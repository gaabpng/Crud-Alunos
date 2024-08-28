def tratar_nota(nota):
    try:
        if nota == '':
            nova_nota = float(0)
        else:
            nova_nota = float(nota)
        return nova_nota
    except ValueError:
        return None

def media(nota_p1, nota_p2, nota_trabalho):
    media_aluno = nota_p1 * 2 + nota_p2 * 2 + nota_trabalho
    media_aluno = media_aluno / 5 
    media_aluno = str(media_aluno)
    return media_aluno

def numeros_na_matricula(matricula):
    matricula = list(matricula)
    try:
        for i in range(len(list(matricula))):
            matricula[i] = int(matricula[i])
        return True
    except ValueError:
        return False
