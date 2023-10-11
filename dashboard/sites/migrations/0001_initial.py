# Generated by Django 4.2.5 on 2023-10-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Borough', models.CharField(default='null', max_length=2, null=True)),
                ('Name', models.CharField(default='null', max_length=50, null=True)),
                ('Location', models.CharField(default='null', max_length=50, null=True)),
                ('Latitude', models.FloatField(default='null', null=True)),
                ('Longitude', models.FloatField(default='null', null=True)),
                ('X', models.DecimalField(decimal_places=5, default='null', max_digits=20, null=True)),
                ('Y', models.DecimalField(decimal_places=5, default='null', max_digits=20, null=True)),
                ('Location_T', models.CharField(default='null', max_length=50, null=True)),
                ('City', models.CharField(default='null', max_length=30, null=True)),
                ('BoroCode', models.IntegerField(default='null', null=True)),
                ('BoroName', models.CharField(default='null', max_length=20, null=True)),
                ('NTACode', models.CharField(default='null', max_length=5, null=True)),
                ('NTAName', models.CharField(default='null', max_length=40, null=True)),
                ('CounDist', models.IntegerField(default='null', null=True)),
                ('Postcode', models.IntegerField(default='null', null=True)),
            ],
        ),
    ]
