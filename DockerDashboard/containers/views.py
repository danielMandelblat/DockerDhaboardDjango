from django.shortcuts import render
from containers.importDataClass import print_all_containers as cn

def index(request):
    data={"title":"Containers", "cn":cn().retrunAsList()}

    return render(request, 'containers.html', data)


def manage_container_main(request, **kwargs):
    if 'container' and 'option' in kwargs:
        from
    data={}
    return render(request, 'manage_container\main.html',data)