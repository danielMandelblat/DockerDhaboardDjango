from django.shortcuts import render, redirect
from servers.models import server
from django.contrib import messages

def index(request):
    #Print all server objects
    servers = server.objects.all()

    data = {"title":"servers", "servers":servers}
    return render(request, 'servers.html', data)

def newServer(request):
    from servers.froms import newServer
    form = newServer()
    if request.method == 'POST':
        form = newServer(request.POST)
        if form.is_valid():
            messages.success(request, f"Host added successfully")
            form.save()
        else:
            messages.error(request, f"Host added failed")

    data = {"title":"New server", "form":form}
    return render(request, 'newServer.html', data)

def removeServer(request):
    if request.method == 'POST':
        serverToDelete=request.POST.get('remove_server')
        current_url=request.POST.get('current_url')

        try:
            ServerToBeDeleted=server.objects.get(host=serverToDelete)
            ServerToBeDeleted.delete()

            messages.success(request, "Server removed successfully")
        except Exception as e:
            messages.warning(request, f"The server didn't found on the DB")
        finally :
            return redirect(current_url)

    else:
         return redirect('/')