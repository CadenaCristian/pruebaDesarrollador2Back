"""pruebaTecnica URL Configuration

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
from .imagenes import listImage, listFavoritos, addFavoritos
from .perros import createDog, listDog, listDogById, updateDog, disableDog, deleteDog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listImage', listImage),
    path('api/listFavoritos', listFavoritos),
    path('api/addFavoritos', addFavoritos),
    path('api/createDog', createDog),
    path('api/listDog', listDog),
    path('api/listDogById/<int:id>', listDogById),
    path('api/updateDog', updateDog),
    path('api/disableDog/<int:id>', disableDog),
    path('api/deleteDog/<int:id>', deleteDog)
]
