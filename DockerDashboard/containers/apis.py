class jsonConvertor:
    def __init__(self, data):
        self.data = data

    def returnAsList(self):
        from json import dumps
        return dumps(self.data)

    def returnAsString(self):
        from json import loads
        return loads(self.data)
class jsonQuery:
    def __init__(self, server, query):
        self.q = query
        self.server = server
    def query(self):
        #returning the data as DIC object
        import requests
        return requests.get(f"http://{self.server.host}:{self.server.port}/{self.q}").json()
    def retuenAsJson(self):
        # returning the data as STR object
        from json import dumps
        return dumps(self.query())

class send_api:
    class containers:
        @staticmethod
        def kill_container(container):
            pass


send_api.containers.kill_container("aa2cde6e9f")