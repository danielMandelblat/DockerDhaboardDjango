from django.urls import path
from servers.views import index
urlpatterns = [
    path("", index, name='base_servers')
]