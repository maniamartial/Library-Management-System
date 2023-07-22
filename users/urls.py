
from django.urls import path

from .import views

urlpatterns=[

    path('register', views.member_registration, name='register'),
    path('login', views.user_login, name='login'),
    path('member', views.add_member, name='member')
]
