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
    def __init__(self, server, port, query):
        self.q = query
        self.server = server
        self.port = port

    def query(self):
        #returning the data as DIC object
        import requests
        return requests.get(f"http://{self.server}:{self.port}/{self.q}").json()

    def query_post(self):
        import requests
        print(f"!!!!!!!!!http://{self.server}:{self.port}/{self.q}")
        result =  requests.post(f"http://{self.server}:{self.port}/{self.q}").status_code

        if result == 204:
            return True
        else:
            return result

    def retuenAsJson(self):
        # returning the data as STR object
        from json import dumps
        return dumps(self.query())
class query_all_servers:
    def __init__(self, url):
        self.url = url

    def printAllServers(self):
        from servers.models import server
        return server.objects.all()

    def query(self):
        data = []
        for s in self.printAllServers():
            data.append({"server":s.host, "port":s.port, "json":jsonQuery(server = s.host, port = s.port, query = self.url).query()})
        return data

#ShortCut to query_all_servers(url).query()
def query(url):
    res = query_all_servers(url).query()
    print(type(res))
    return res