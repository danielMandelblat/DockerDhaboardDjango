from django.urls import path
from servers.views import index, newServer, removeServer

urlpatterns = [
    path("", index, name='base_servers'),
    path("newServer/", newServer, name='new_server'),
    path("removeServer", removeServer, name='remove_server'),
]