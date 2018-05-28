from django.urls import path
from .views import *
urlpatterns = [
    path('', home_page, name='home_page'),
    path('book/', create_book, name='create_book'),
    path('book/<int:id>',update_book, name='update_book')
]