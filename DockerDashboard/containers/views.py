from django.shortcuts import render, redirect
from containers.importDataClass import print_all_containers as cn
from django.views.decorators.clickjacking import xframe_options_exempt




def index(request):
    data={"title":"Containers", "cn":cn().retrunAsList(),
          "container" : "test2"}
    return render(request, 'containers.html', data)

@xframe_options_exempt
def manage_container_main(request, **kwargs):
    if 'container' and 'option' in kwargs:
        #Collect all data about the container
        from containers.importDataClass import print_container_infomration as containerInfo

        data = {"container": kwargs ['container']}

        #Add values to data dic
        data['c'] = containerInfo(kwargs ['container']).retrunQuery

        data['db'] = containerInfo.return_container_object_from_db(containerId = kwargs['container'])

        if kwargs['option'] == 'main':
            return render(request, r'manage_container\main.html', data)

def container_action(request, container, action):
    print(f"!!!!container: {container}  | action: {action}")
    return redirect(manage_container_main, container=container, option='main')