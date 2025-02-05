from django.shortcuts import render
from django.http import HttpResponse
from .utils import google_search
from django.http import JsonResponse
from django.shortcuts import render
from .models import ErrorLog


def index(request):
    return render(request, 'index.html', status=200)

def show_error_404(request):
    return render(request, '404.html', status=404)

def show_error_505(request):
    return render(request, '505.html', status=505)

def generar_error(request):
    return 7/0

def onepage(request):
    return render(request, 'onepage.html',status=200)

def prueba(request):
    nombre = request.GET.get('nombre','')
    edad = request.GET.get('edad','')
    persona={
        'nombre': nombre,
        'edad': edad,
        'descripcion': nombre + " - " + edad
    }

    persona2={
        'nombre': 'Nancy',
        'edad': '30',
        'descripcion': nombre + " - " + edad
    }

    persona3={
        'nombre': 'Alexis',
        'edad': '24',
        'descripcion': nombre + " - " + edad
    }

    if(persona['nombre'] == 'Miku'):
        persona['descripcion'] = 'Bienvenido reinota'

    print(persona['nombre'])
    conjunto = [persona,persona2,persona3]

    return render(
    request,
    'prueba.html',
    {'objeto':persona, 'saludo':'Hola chat','personas':conjunto}
)

def busqueda(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "busqueda.html", {"results": results, "query": query})



def error_logs(request):
    return render(request, 'errorlogs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})