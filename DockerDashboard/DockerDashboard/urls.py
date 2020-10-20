from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('containers/', include('containers.urls')),
    path('servers/', include('servers.urls')),
]
