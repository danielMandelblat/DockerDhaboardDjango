from django.db import models
from django.core.exceptions import ValidationError


class server(models.Model):
    name = models.CharField(max_length=250, unique=True, default=None)
    host = models.CharField(max_length=50, primary_key=True, unique=True)
    port = models.PositiveIntegerField()
    dateCreated = models.DateTimeField(auto_now_add=True, blank=True)
    lastCheck = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, editable=False)

    def clean(self):
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((self.host,self.port))
            print(f"result: {result}")
            if result == 0:
                self.status = True
            else:
                raise ValidationError(f"The {self.host}:{self.port} not response")


        except Exception as e:
            print(e)
            raise ValidationError(e)

    def __str__(self):
        return f"Machine: (name: {self.name}, host: {self.host}, port: {self.port})"


