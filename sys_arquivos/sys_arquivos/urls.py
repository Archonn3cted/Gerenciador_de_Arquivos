"""
URL configuration for sys_arquivos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from gerenciamento_arquivos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('criar/', views.criar_arquivo, name='criar_arquivo'),
    path('ler/<str:nome>/', views.ler_arquivo, name='ler_arquivo'),
    path('deletar/<str:nome>/', views.deletar_arquivo, name='deletar_arquivo'),
    path('', views.lista_arquivos, name='lista_blocos'),
]
