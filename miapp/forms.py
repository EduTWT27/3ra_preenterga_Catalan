from django import forms
from .models import Autor, Libro, Review

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
