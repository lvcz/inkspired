from django.urls import path
from .views import *
urlpatterns = [
    path('', home_page, name='home_page'),
    path('book/', create_book, name='create_book'),
    path('book/<int:id>/update/', update_book, name='update_book'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('book/<int:id>/delete/', delete_book, name='delete_book'),
    path('book/<int:id>/create_chapter/', create_chapter, name='create_chapter'),
    path('chapter/<int:id>/edit/', edit_chapter, name='edit_chapter'),
    path('chapter/<int:id>/delete/', delete_chapter, name='delete_chapter'),
    path('book/<int:id>/download/', download_pdf, name='download_pdf'),
]
