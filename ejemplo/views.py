from django.shortcuts import render

# Create your views here. 
#Rivisar hora 8:50

def index(request):
    sum = 15 + 18
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre":"Osvaldo",
        "apellido":"Castrejon",
        "suma": sum
    })


def index_dos (request, nombre, apellido):
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre":"Osvaldo",
        "apellido":"Castrejon",
    })

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {
        "notas":[1,2,3,4,5,6,7,8]
    })

def imc(request, peso, altura):
    imc = peso * altura
    return render(request, "ejemplo/imc.html", {"imc": imc})
