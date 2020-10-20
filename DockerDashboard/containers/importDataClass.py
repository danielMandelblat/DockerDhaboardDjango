import requests
from containers.models import container


class importData():
        class container:
            def __init__(self, id, names, image, imageID, command, created, ports):
                self.id = id
                self.names = names
                self.imageID = imageID
                self.command = command
                self.created = created
                self.ports = ports
            def __str__(self):
                return f"Container class: (id:{self.id}, names:{self.names})"

        @staticmethod
        def print_container_info(containerId):
            url = "http://10.100.102.52:2375/containers/json"
            result = requests.get(url).json()
            for line in result:
                print(line)

