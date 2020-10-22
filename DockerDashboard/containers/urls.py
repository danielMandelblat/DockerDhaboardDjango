from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_containers"),
    path('<str:container>/manage/<str:option>/', views.manage_container_main),
]
