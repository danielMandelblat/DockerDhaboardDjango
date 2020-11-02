from django.urls import path
from  networks.views import networks

urlpatterns = [
    path('', networks, name='index_networks'),
]