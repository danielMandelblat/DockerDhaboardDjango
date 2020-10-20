from django.shortcuts import render
from .importDataClass import importData

def index(request):
    #import containers data
    importData.print_container_info("dfdf")

    return render(request, 'index.html')