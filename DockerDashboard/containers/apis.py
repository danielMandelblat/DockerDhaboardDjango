class jsonConvertor:
    def __init__(self, data):
        self.data = data

    def returnAsList(self):
        from json import dumps
        return dumps(self.data)

    def returnAsString(self):
        from json import loads
        return loads(self.data)

class apis:
    @staticmethod
    def containers():
        data = {"print_all_containers" : "containers/json?all=true",
                }
        return data

