from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('author/Jane-Austen/', views.Austen, name='Austen'),
    path('author/Albert-Einstein/', views.Einstein, name='Einstein'),
    path('author/J-K-Rowling/', views.Rowling, name='Rowling'),
    path('author/Andre-Gide/', views.Gide, name='Gide'),
    path('author/Marilyn-Monroe/', views.Monroe, name='Monroe'),
    path('author/Thomas-A-Edison/', views.Edison, name='Edison'),
    path('author/Eleanor-Roosevelt/', views.Roosevelt, name='Roosevelt'),
    path('author/Steve-Martin/', views.Martin, name='Martin'),
]
