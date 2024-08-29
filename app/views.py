from django.shortcuts import get_object_or_404, render
from .models import Alunos
from django.shortcuts import redirect
from .functions import tratar_nota, media, numeros_na_matricula

def home(request):
    return render(request, 'home.html') # retorna a pagina home.html

def adicionar_aluno(request):
    if request.method == 'POST':
        nota_p1 = tratar_nota(request.POST['nota_p1'])
        nota_p2 = tratar_nota(request.POST['nota_p2'])
        nota_trabalho = tratar_nota(request.POST['nota_trabalho'])
        
        if nota_p1 is None or nota_p2 is None or nota_trabalho is None:
            return render(request, 'adicionar_err_matricula.html') # retorna página de erro de nota

        if numeros_na_matricula(request.POST['matricula']):
            if len(request.POST['matricula']) == 9:
                novo_aluno = Alunos(
                    nome=request.POST['nome'],
                    matricula=request.POST['matricula'],
                    nota_p1=str(nota_p1),
                    nota_p2=str(nota_p2),
                    nota_trabalho=str(nota_trabalho),
                    media=media(nota_p1, nota_p2, nota_trabalho)
                )
                novo_aluno.save()
                return render(request, 'adicionar.html') 
            else:
                return render(request, 'adicionar_err_matricula.html') # retorna página de erro de matrícula

        else:
            return render(request, 'adicionar_err_matricula.html') # retorna página de erro de matrícula

    return render(request, 'adicionar.html') 

def adicionar_aluno_erro(request):
    if request.method == 'POST':
        nota_p1 = tratar_nota(request.POST['nota_p1'])
        nota_p2 = tratar_nota(request.POST['nota_p2'])
        nota_trabalho = tratar_nota(request.POST['nota_trabalho'])
        
        if nota_p1 is None or nota_p2 is None or nota_trabalho is None:
            return render(request, 'adicionar_err_nota.html') # retorna página de erro de nota

        if numeros_na_matricula(request.POST['matricula']):
            if len(request.POST['matricula']) == 9:
                novo_aluno = Alunos(
                    nome=request.POST['nome'],
                    matricula=request.POST['matricula'],
                    nota_p1=str(nota_p1),
                    nota_p2=str(nota_p2),
                    nota_trabalho=str(nota_trabalho),
                    media=media(nota_p1, nota_p2, nota_trabalho)
                )
                novo_aluno.save()
                return render(request, 'adicionar.html') 
            else:
                return render(request, 'adicionar_err_matricula.html') # retorna página de erro de matrícula

        else:
            return render(request, 'adicionar_err_matricula.html') # retorna página de erro de matrícula

    return render(request, 'adicionar.html') 

def listar_aluno(request):
    alunos = {
        'alunos': Alunos.objects.all()
    }
    return render(request, 'listar.html', alunos) 

def deletar_aluno(request, id_aluno):
    Alunos.objects.filter(id_aluno=id_aluno).delete()
    return redirect('listar_aluno')

def teste(request):
    return render(request, 'test.html') 

def editar_aluno(request, id_aluno):
    aluno = get_object_or_404(Alunos, id_aluno=id_aluno)

    if request.method == 'POST':
        # Trata as notas recebidas do formulário
        nota_p1 = tratar_nota(request.POST['nota_p1'])
        nota_p2 = tratar_nota(request.POST['nota_p2'])
        nota_trabalho = tratar_nota(request.POST['nota_trabalho'])
        
        if nota_p1 is None or nota_p2 is None or nota_trabalho is None:
            return render(request, 'adicionar_err_nota.html')  # Retorna página de erro de nota

        if numeros_na_matricula(request.POST['matricula']):
            if len(request.POST['matricula']) == 9:
                # Atualiza os campos do aluno
                aluno.nome = request.POST['nome']
                aluno.matricula = request.POST['matricula']
                aluno.nota_p1 = nota_p1
                aluno.nota_p2 = nota_p2
                aluno.nota_trabalho = nota_trabalho
                aluno.media = media(nota_p1, nota_p2, nota_trabalho)
                aluno.save()

                return redirect('listar_aluno')  # Redireciona para a lista de alunos após a edição
            else:
                return render(request, 'adicionar_err_matricula.html')  # Retorna página de erro de matrícula
        else:
            return render(request, 'adicionar_err_matricula.html')  # Retorna página de erro de matrícula

    # Renderiza o template de adição com os dados do aluno preenchidos para edição
    return render(request, 'editar.html', {'aluno': aluno})
