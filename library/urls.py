from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add_book', views.add_book, name='add_book'),
    path('book_listing', views.all_books, name='book_listing'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('create_transaction/<int:book_id>/', views.create_transaction, name="create_transaction"),
    path('transaction_list', views.transaction_list, name='transaction_list'),
    path('update_transaction/<transaction_id>/', views.update_transaction, name="update_transaction"),
    path("delete_transaction/<transaction_id>/", views.delete_transaction, name="delete_transaction"),

    path("add_member", views.add_member, name="add_member")

]
