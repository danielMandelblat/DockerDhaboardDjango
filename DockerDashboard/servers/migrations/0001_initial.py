# Generated by Django 3.1.2 on 2020-10-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='server',
            fields=[
                ('name', models.CharField(default=None, max_length=250, unique=True)),
                ('host', models.GenericIPAddressField(primary_key=True, serialize=False, unique=True)),
                ('port', models.IntegerField()),
                ('dataAdded', models.DateTimeField(auto_now_add=True)),
                ('lastCheck', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False, editable=False)),
            ],
        ),
    ]
