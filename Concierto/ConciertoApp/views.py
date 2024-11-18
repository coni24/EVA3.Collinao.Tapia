from django.shortcuts import render,redirect
from ConciertoApp.models import Entrada, Persona, Concierto
from ConciertoApp.forms import FormEntrada, FormPersona, FormConcierto

#Vista Entradas
def index(request):
    return render(request,'templateApp/index.html')

def listaEntrada(request):
    entradas = Entrada.objects.all()
    data = {'entradas': entradas}
    return render(request,'templateApp/entradas.html',data)

def agregarEntrada(request):
    form = FormEntrada()
    if request.method == 'POST':
        form = FormEntrada(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/entradas')
        else:
            print(form.errors)
            return render(request, 'templateApp/agregarEntrada.html', {'form': form})
    
    data = {'form': form}
    return render(request,'templateApp/agregarEntrada.html',data)

def eliminarEntrada(request,id):
    entrada = Entrada.objects.get(id = id)
    entrada.delete()
    return redirect('/entradas')

def actualizarEntrada(request,id):
    entrada = Entrada.objects.get(id = id)
    form = FormEntrada(instance=entrada)
    if request.method == 'POST':
        form = FormEntrada(request.POST,instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('/entradas')
        else:
            print(form.errors)
            return render(request, 'templateApp/agregarEntrada.html', {'form': form})
    data = {'form' : form}
    return render(request,'templateApp/agregarEntrada.html',data)

#Vista Persona

def listaPersona(request):
    personas = Persona.objects.all()
    data = {'personas': personas}
    return render(request,'templateApp/personas.html', data)

def agregarPersona(request):
    form = FormPersona()
    if request.method == 'POST':
        form = FormPersona(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/personas')
    data = {'form': form}
    return render(request,'templateApp/agregarPersona.html',data)

def eliminarPersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('/personas')

def actualizarPersona(request,id):
    persona = Persona.objects.get(id = id)
    form = FormPersona(instance=persona)
    if request.method == 'POST':
        form = FormPersona(request.POST,instance=persona)
        if form.is_valid():
            form.save()
            return redirect('/personas')
    data = {'form' : form}
    return render(request,'templateApp/agregarPersona.html',data)


#Vista Concierto

def listaConcierto(request):
    conciertos = Concierto.objects.all()
    data = {'conciertos': conciertos}
    return render(request, 'templateApp/conciertos.html',data)

def agregarConcierto(request):
    form = FormConcierto()
    if request.method == 'POST':  
        form = FormConcierto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/conciertos')
        else:
            print(form.errors)
            return render(request, 'templateApp/agregarConcierto.html', {'form': form})
    
    data = {'form': form}
    return render(request, 'templateApp/agregarConcierto.html', data)

def eliminarConcierto(request, id):
    concierto = Concierto.objects.get(id=id)
    concierto.delete()
    return redirect('/conciertos')

def actualizarConcierto(request, id):
    concierto = Concierto.objects.get(id=id)
    form = FormConcierto(instance=concierto)
    if request.method == 'POST':
        form = FormConcierto(request.POST, instance=concierto)
        if form.is_valid():
            form.save()
            return redirect('/conciertos')
        else:
            print(form.errors)
            return render(request, 'templateApp/agregarConcierto.html', {'form': form})

    data = {'form': form}
    return render(request, 'templateApp/agregarConcierto.html', data)
