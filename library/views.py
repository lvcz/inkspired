from django.shortcuts import render, redirect
from .models import Book, Chapter
from .forms import BookForm, ChapterForm


def home_page(request):
    books = Book.objects.all()

    return render(request, 'home.html', {'books': books})


def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    url = '/book/'
    if form.is_valid():
        form.save()
        return redirect('home_page')

    return render(request, 'form.html', {'form': form, 'url': url})


def book_detail(request, id):
    book = Book.objects.get(id=id)
    try:
        chapters = Chapter.objects.all().filter(book=book)
    except Exception as ex:
        chapters = []
    return render(request, 'book.html', {'book': book, 'chapters': chapters})


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    url = '/book/{}/update/'.format(id)
    if form.is_valid():
        form.save()
        return redirect('home_page')

    return render(request, 'form.html', {'form': form, 'book': book, 'url': url})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home_page')


def create_chapter(request, id):
    form = ChapterForm(request.POST or None)
    url = '/book/{}/create_chapter/'.format(id)
    if form.is_valid():
        chapter = form.save(commit=False)
        chapter.book_id = id
        chapter.save()

        return redirect('home_page')
    return render(request, 'form.html', {'form': form, 'url': url})


def edit_chapter(request, id):
    chapter = Chapter.objects.get(id=id)
    form = ChapterForm(request.POST or None, instance=chapter)
    url = '/chapter/{}/edit/'.format(id)
    if form.is_valid():
        form.save()
        return redirect('home_page')
    return render(request, 'form.html', {'form': form, 'url': url})


def delete_chapter(request, id):
    chapter = Chapter.objects.get(id=id)
    if request.method == 'POST':
        chapter.delete(keep_parents=True)
        return redirect('home_page')
