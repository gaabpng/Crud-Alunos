from django.shortcuts import render
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
