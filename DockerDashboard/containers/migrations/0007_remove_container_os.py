# Generated by Django 3.1.2 on 2020-10-24 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0006_auto_20201025_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='os',
        ),
    ]