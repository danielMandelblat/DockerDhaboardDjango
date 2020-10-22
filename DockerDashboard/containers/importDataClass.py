import requests
from containers import apis
#Class
#================================
class container:
    def __init__(self , id , names , image , imageID , command , created , ports, Labels, State, Status, HostConfig, NetworkSettings, Mounts):
        self.id = id[:10]
        self.names = names[0]
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

    def __str__(self):
        return f"Container class: (id:{self.id}, names:{self.names})"
    list = []
    string = ""
class jsonQuery:
    def __init__(self, server, query):
        self.q = query
        self.server = server
    def query(self):
        return requests.get(f"http://{self.server.host}:{self.server.port}/{self.q}").json()
    def retuenAsJson(self):
        from json import dumps
        return dumps(self.query())
def testJson():
    from servers.models import server
    s = server.objects.all()[0]
    #from containers.apis import apis
    d = apis.apis.containers()['print_all_containers']
    return jsonQuery(s, d).retuenAsJson()



class print_all_containers():
    containers = []
    def __init__(self):
        self.containers = []

        from servers.models import server
        servers = server.objects.all()
        url = apis.apis.containers() ['print_all_containers']

        #For each server bring containers
        for server in servers:
            if len(servers) != 0:
                api = jsonQuery(server,url).query()
                for c in api:
                    # Collect all returned containers to list as objects
                    self.containers.append(container(id = c ['Id'] , names = c ['Names'] , image = c ['Image'] ,
                                                     imageID = c ['ImageID'] , command = c ['Command'] ,
                                                     created = c ['Created'] , ports = c ['Ports'] ,
                                                     Labels = c ['Labels'] , State = c ['State'] ,
                                                     Status = c ['Status'] ,
                                                     HostConfig = c ['HostConfig'] ,
                                                     NetworkSettings = c ['NetworkSettings'] ,
                                                     Mounts = c ['Mounts']))
    def retrunAsList(self):
        return self.containers


