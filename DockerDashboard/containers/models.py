from django.db import models

class container(models.Model):
    id = models.CharField(max_length=50, null=False, blank=False, primary_key=True, unique=True)

class server(models.Model):
    host = models.CharField(max_length=50, primary_key=True, unique=True)
    port = models.CharField(max_length=6)
    lastCheck = models.CharField(max_length=20)
