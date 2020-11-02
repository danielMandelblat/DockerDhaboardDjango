from django.contrib import admin
from servers.models import server

#Edit server model
class serverValidate(admin.ModelAdmin):
    readonly_fields = ['status']

#Register server model -
admin.site.register(server, serverValidate)