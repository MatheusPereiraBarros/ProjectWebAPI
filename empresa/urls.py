"""gerenbus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from empresa import views
from django.conf.urls.static import static
from .views import *


router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'viagens', views.viagens_list)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^viagens$', views.viagens_list),
    url(r'^viagem$/(?P<pk>[0-9]+)/$', views.viagens_detail),
    url(r'^funcionarios$', views.funcionarios_list),
    url(r'^funcoes$', views.funcoes_list),
    url(r'^rotas$', views.rotas_list),
    url(r'^onibus$', views.onibus_list),
    url(r'^users/$', UserList.as_view(), name=UserList.name),
    url(r'^garagens$', views.garagens_list),
 ]
    #url(r'^apiauth/', include('rest_framework.urls', namespace='rest_framework'))


