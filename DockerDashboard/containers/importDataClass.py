import requests
from containers.models import container
#Class
#================================
class container:
    def __init__(self , id , names , image , imageID , command , created , ports, Labels, State, Status, HostConfig, NetworkSettings, Mounts, server, server_port ):
        self.id = id[:10]
        self.names = str(names[0]).split("/")[1]
        self.image = image[:10]
        self.imageID = imageID[:10]
        self.command = command[:20]
        self.created = created
        self.ports = ports
        self.Labels = Labels
        self.State = State
        self.Status= Status
        self.HostConfig = HostConfig
        self.NetworkSettings = NetworkSettings
        self.Mounts = Mounts
        self.server = server
        self.server_port = server_port

    def __str__(self):
        return f"Container class: (id:{self.id}, names:{self.names})"
    list = []
    string = ""

class jsonQuery:
    def __init__(self, server, port, query):
        self.q = query
        self.server = server
        self.port = port
    def query(self):
        #returning the data as DIC object
        return requests.get(f"http://{self.server}:{self.port}/{self.q}").json()
    def retuenAsJson(self):
        # returning the data as STR object
        from json import dumps
        return dumps(self.query())

class print_all_containers():
    containers = []
    def __init__(self):
        self.containers = []

        from servers.models import server
        servers = server.objects.all()
        url = "containers/json?all=true"

        #For each server bring containers
        for server in servers:
            if len(servers) != 0:
                api = jsonQuery(server,url).query()
                for c in api:
                    # Collect all returned containers to list as objects
                    current_container = container(id = c ['Id'] , names = c ['Names'] , image = c ['Image'] ,
                                                     imageID = c ['ImageID'] , command = c ['Command'] ,
                                                     created = c ['Created'] , ports = c ['Ports'] ,
                                                     Labels = c ['Labels'] , State = c ['State'] ,
                                                     Status = c ['Status'] ,
                                                     HostConfig = c ['HostConfig'] ,
                                                     NetworkSettings = c ['NetworkSettings'] ,
                                                     Mounts = c ['Mounts'], server = f"{server.host}",
                                                     server_port = f"{server.port}")
                    #Add to 'containers' list
                    self.containers.append(current_container)

                    #Push 'container' object to DB
                    print_container_infomration.push_container_to_db(current_container)

    def retrunAsList(self):
        return self.containers

class print_container_infomration:
    json = ""
    def __init__(self, container):
        self.container = container

        #select Server
        from servers.models import server

        server = container.objects.filter(id='aa2cde6e9f').first().container_server.host
        port = container.objects.filter(id='aa2cde6e9f').first().container_server.port


        #Build url path for the json query
        q = f"containers/{self.container}/json"

        #Create a new API query
        self.json =  jsonQuery(server, port, q).query()

    def retrunQuery(self):
        #Return JSON data
        return self.json

    @staticmethod
    def print_container_server(c):
        container.objects.filter(id=c.id).first()
        return container.container_server

    @staticmethod
    def push_container_to_db(c):
        from servers.models import server
        from containers.models import container

        filterd_server = server.objects.filter(host = f'{c.server}', port=f"{c.server_port}").first()
        current_container = container(id=c.id, name=c.names, image=c.image, container_server=filterd_server)
        current_container.save()



