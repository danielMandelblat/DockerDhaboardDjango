from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_containers"),
    path(r'<str:container>/manage/<str:option>/', views.manage_container_main, name="container_manage"),
    path(r'<str:action>/<str:container>/', views.container_action, name="container_action"),
]
