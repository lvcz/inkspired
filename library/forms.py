from django import forms
from .models import Book, Chapter

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'category', 'author', 'date_created', 'front_cover']