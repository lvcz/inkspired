from django.urls import path
from .views import home_page, create_book
urlpatterns = [
    path('', home_page, name='home_page'),
    path('book', create_book, name='create_book')
]