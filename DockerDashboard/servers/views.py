from django.shortcuts import render

def index(request):
    data = {"title" : "servers"}
    return render(request, 'index_servers.html', data)