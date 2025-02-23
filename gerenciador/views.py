from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import(
    TbCampanhas,
    TbModelo_Cesta,
    TbAsItem_Modelo,
    TbItem_Cesta,
)
from .forms import ModeloCestaForm,CampanhaForm
from .controls import analisar_metas

#autenticação
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Conta criada com sucesso para {username}!')
            return redirect('campanhas')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Você está logado como {username}.')
                return redirect('campanhas')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Você foi deslogado com sucesso.')
    return redirect('login')
#------------------------------------------------------------------------
#CRUD das Campanhas

def editar_campanha(request, campanha_id):
    campanha = get_object_or_404(TbCampanhas, ID_Campanha=campanha_id)
    
    if request.method == "POST":
        campanha.Titulo = request.POST.get("Titulo")
        campanha.Prazo = request.POST.get("Prazo")
        campanha.Quantidade_Cestas = request.POST.get("Quantidade_Cestas")
        campanha.status = analisar_metas(campanha.ID_Campanha)
        campanha.save()
        return redirect("campanhas") 
    
    return render(request, "editar-campanha.html", {"campanha": campanha})

def buscar_campanhas(request):
    query = request.GET.get('q') 
    Campanhas = TbCampanhas.objects.all()  

    if query:
        Campanhas = Campanhas.filter(name__icontains=query) 

    return render(request, 'campanhas.html', {'campanhas': Campanhas, 'query': query})

def criar_campanha(request, campanha_id=None):
    campanha = get_object_or_404(TbCampanhas, ID_Campanha=campanha_id) if campanha_id else None

    if request.method == "POST":
        form = CampanhaForm(request.POST, instance=campanha)
        if form.is_valid():
            campanha = form.save()
            campanha.status = analisar_metas(campanha.ID_Campanha)
            return redirect("campanhas")
    else:
        form = CampanhaForm(instance=campanha)

    return render(request, "criar-campanha.html", {"form": form})


def deletar_campanha(request, campanha_id):
    campanha = get_object_or_404(TbCampanhas, ID_Campanha=campanha_id)
    
    if request.method == "POST":
        campanha.delete()
        return redirect("campanhas") 

    return render(request, "excluir-campanha.html", {"campanha": campanha})
#----------------------------------------------------------------------

#CRUD Das Cestas Básicas
def buscar_Cestas_Basicas(request):
    query = request.GET.get('q') 
    Cestas_Basicas = TbModelo_Cesta.objects.all()  

    if query:
        Cestas_Basicas = Cestas_Basicas.filter(name__icontains=query) 

    return render(request, 'Cestas-Basicas.html', {'Cestas_Basicas': Cestas_Basicas, 'query': query})

def criar_cesta_basica(request):
    if request.method == "POST":
        form = ModeloCestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cestas_basicas")  # Redireciona para a lista de cestas após criar
    else:
        form = ModeloCestaForm()

    return render(request, "criar-cesta-basica.html", {"form": form})

def editar_cesta_basica(request, cesta_id):
    cesta = get_object_or_404(TbModelo_Cesta, id_Cesta=cesta_id)

    if request.method == "POST":
        form = ModeloCestaForm(request.POST, instance=cesta)
        if form.is_valid():
            form.save()
            return redirect("cestas_basicas")  # Redireciona para a lista de cestas após a edição
    else:
        form = ModeloCestaForm(instance=cesta)

    return render(request, "editar-cesta-basica.html", {"form": form, "cesta": cesta})


def deletar_cesta_basica(request, cesta_id):
    cesta = get_object_or_404(TbModelo_Cesta, id_Cesta=cesta_id)

    if request.method == "POST":
        cesta.delete()
        return redirect("cestas_basicas")  # Redireciona para a lista após a exclusão

    return render(request, "excluir-cesta-basica.html", {"cesta": cesta})

#------------------------------------------------------------------------

#CRUD dos Itens
def buscar_Itens(request):
    query = request.GET.get('q') 
    Itens_Cesta = TbItem_Cesta.objects.all()  

    if query:
        Itens_Cesta = Itens_Cesta.filter(name__icontains=query) 

    return render(request, 'Estoque.html', {'Itens_Cesta': Itens_Cesta, 'query': query})

def analisar_cestas(request):
    pass

