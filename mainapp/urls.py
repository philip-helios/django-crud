from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('',views.add_show, name="addandshow")
]