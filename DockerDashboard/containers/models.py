from django.db import models
from datetime import datetime

class container(models.Model):
    from servers.models import server
    id = models.CharField(primary_key = True, max_length = 250, unique = True)
    name = models.CharField(max_length = 150, default = None, unique = True)
    image = models.CharField(max_length = 150, default = None)
    lastCheck = models.DateTimeField(default = datetime.now)

    container_server = models.ForeignKey(server, on_delete = models.CASCADE)


class tag(models.Model):
    name = models.CharField(max_length = 250, unique = True)
    id = models.CharField(max_length = 100, unique = True, primary_key = True)


