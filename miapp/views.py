
# Create your views here.
from django.shortcuts import render, redirect
from .models import Autor, Libro, Review
from .forms import AutorForm, LibroForm, ReviewForm

def autor_form(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio después de guardar
    else:
        form = AutorForm()
    return render(request, 'autor_form.html', {'form': form})

def libro_form(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LibroForm()
    return render(request, 'libro_form.html', {'form': form})

def review_form(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def buscar(request):
    if request.method == "POST":
        query = request.POST.get('query')
        resultados = Libro.objects.filter(titulo__icontains=query)  # Busca libros por título
        return render(request, 'resultados.html', {'resultados': resultados})
    return render(request, 'buscar.html')
