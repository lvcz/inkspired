from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def home_page(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home_page')

    return render(request, 'book-form.html', {'form': form})

#
# def update_product(request, id):
#     # product = Product.objects.get(id=id)
#     # form = ProductForm(request.POST or None, instance=product)
#
#     if form.is_valid():
#         form.save()
#         return redirect('list_products')
#
#     return render(request, 'products-form.html', {'form': form, 'product': product})
#
#
# def delete_product(request, id):
#     product = Product.objects.get(id=id)
#
#     if request.method == 'POST':
#         product.delete()
#         return redirect('list_products')
#
#     return render(request, 'prod-delete-confirm.html', {'product': product})