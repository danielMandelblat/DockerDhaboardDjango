from django.db import models

class container(models.Model):
    id = models.CharField(max_length=50, null=False, blank=False, primary_key=True, unique=True)
    names = models.CharField(max_length = 150, default = None)
    image = models.CharField(max_length = 150, default = None)
    os = models.CharField(max_length = 150, default = None)
    server = models.CharField(max_length = 150, default = None)

