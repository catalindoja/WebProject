# Generated by Django 4.0.3 on 2022-03-15 15:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('telephone', models.DecimalField(decimal_places=0, max_digits=9)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('dateLatestVisit', models.DateField(default=datetime.date.today)),
                ('latestZooVisited', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('age', models.DateField(default=datetime.date.today)),
                ('address', models.CharField(max_length=80)),
                ('postalcode', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Postal code')),
            ],
        ),
        migrations.CreateModel(
            name='Zoo',
            fields=[
                ('zoo_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
                ('max_visitors', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Max amount of visitors')),
                ('address', models.CharField(max_length=80)),
                ('postalcode', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Postal code')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('worker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='zooproject.worker')),
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('assigned_habitat', models.CharField(default='Dolphins', max_length=80)),
            ],
            bases=('zooproject.worker',),
        ),
        migrations.CreateModel(
            name='Veterinary',
            fields=[
                ('worker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='zooproject.worker')),
                ('vet_id', models.AutoField(primary_key=True, serialize=False)),
                ('assigned_animals', models.IntegerField()),
            ],
            bases=('zooproject.worker',),
        ),
    ]
