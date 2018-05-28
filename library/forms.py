from django import forms
from .models import Book, Chapter

class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    category= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    author= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    front_cover = forms.ImageField(required=False, label_suffix='front cover')


    class Meta:
        model = Book
        fields = ['title', 'description', 'category', 'author', 'front_cover']