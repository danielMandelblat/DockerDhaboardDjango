from django.db import models
import json

def covertListToJson(list):
    import json

class container(models.Model):
    id = models.CharField(max_length=50, null=False, blank=False, primary_key=True, unique=True)
    names = models.CharField(max_length = 150)
    image = models.CharField(max_length = 150)
    imageID = models.CharField(max_length = 150)
    command = models.CharField(max_length = 500)
    created = models.DateTimeField(blank = True, null = True)

