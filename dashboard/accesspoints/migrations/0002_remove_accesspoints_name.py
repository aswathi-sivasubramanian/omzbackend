# Generated by Django 4.2.5 on 2023-10-05 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accesspoints', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesspoints',
            name='name',
        ),
    ]