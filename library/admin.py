from django.contrib import admin
from .models import Book, Transaction, Member

# Register your models here.


admin.site.register(Book)
admin.site.register(Transaction)
admin.site.register(Member)