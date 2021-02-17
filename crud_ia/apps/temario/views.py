from django.shortcuts import render, redirect
from apps.temario.models import Temario

# Create your views here.
def index_temario(request):
    temario_lista = Temario.objects.all()
    return render(request, template_name='temario/index.html', context={'temario_lista': temario_lista})

def crear_tema(request):
    if request.method == 'POST':
        numero = request.POST['numero']
        nombre = request.POST['nombre']
        Temario.objects.create(numero=numero, nombre=nombre)
    return render(request, template_name='temario/create.html')

def editar_tema(request, id):
    tema = Temario.objects.get(id=id)

    if request.method == 'POST':
        numero = request.POST['numero']
        nombre = request.POST['nombre']

        tema.save()
    return render(request, 'temario/create.html', {'tema': tema})        

def borrar_tema(request, id):
    tema = Temario.objects.get(id=id).delete()
    return redirect('index')


