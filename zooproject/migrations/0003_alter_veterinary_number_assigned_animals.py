# Generated by Django 4.0.2 on 2022-04-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooproject', '0002_alter_worker_age_alter_worker_postalcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinary',
            name='number_assigned_animals',
            field=models.IntegerField(null=True),
        ),
    ]
