from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home', views.home, name="home"),
    path('add', views.addstd, name="addstd"),
    path('delete/<int:roll>', views.delete, name="delete_std"),
    path('update/<int:roll>', views.update, name="update_std"),
    path('do-update/<int:id>', views.do_update, name="do-update_std"),

]
