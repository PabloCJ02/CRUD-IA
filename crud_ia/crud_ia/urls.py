"""crud_ia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from apps.temario.views import index_temario, crear_tema, editar_tema, borrar_tema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_temario, name='index'),
    path('crear/', crear_tema, name='crear'),
    path('editar/<int:id>/', editar_tema, name='editar'),
    path('borrar/<int:id>/', borrar_tema, name='borrar'),
]
