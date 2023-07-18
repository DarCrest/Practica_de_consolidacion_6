"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import (
    index,
    vehiculo_add,
    vehiculo_list,
    login_,
    register,
    logout_
)

urlpatterns = [
    path("", index, name="index"),
    path("vehiculo/add/", vehiculo_add, name="vehiculo_add"),
    path("vehiculo/list/", vehiculo_list, name="vehiculo_list"),
    path("login/", login_, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_, name="logout")

]
