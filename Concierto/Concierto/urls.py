"""Concierto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ConciertoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('entradas/', views.listaEntrada, name='entradas'),
    path('agregarEntrada/',views.agregarEntrada),
    path('eliminarEntrada/<int:id>', views.eliminarEntrada),
    path('actualizarEntrada/<int:id>',views.actualizarEntrada),

    path('personas/', views.listaPersona, name='personas'),
    path('agregarPersona/', views.agregarPersona),
    path('eliminarPersona/<int:id>/', views.eliminarPersona),
    path('actualizarPersona/<int:id>/', views.actualizarPersona),

    path('conciertos/', views.listaConcierto, name='conciertos'),
    path('agregarConcierto/', views.agregarConcierto),
    path('eliminarConcierto/<int:id>/', views.eliminarConcierto),
    path('actualizarConcierto/<int:id>/', views.actualizarConcierto),
]
