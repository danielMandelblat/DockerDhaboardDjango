from django.urls import path
from servers.views import index, newServer, removeServer

urlpatterns = [
    path("", index, name='index_servers'),
    path("newServer/", newServer, name='new_server'),
    path("removeServer", removeServer, name='remove_server'),
]