from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def home_page(request):
    books = Book.objects.all()

    return render(request, 'home.html', {'books': books})


def create_book(request):
    form = BookForm(request.POST or None)
    url = '/book/'
    if form.is_valid():
        form.save()
        return redirect('home_page')

    return render(request, 'form.html', {'form': form, 'url': url})


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'form.html', {'form': form, 'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('home_page')