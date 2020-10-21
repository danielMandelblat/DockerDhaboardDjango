from django.forms import ModelForm
from servers.models import server

class newServer(ModelForm):
    class Meta:
        model = server
        fields = ['name','host', 'port']

