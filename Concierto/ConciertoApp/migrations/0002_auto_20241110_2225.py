# Generated by Django 3.2 on 2024-11-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConciertoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='Edad',
        ),
        migrations.AlterField(
            model_name='concierto',
            name='Categoria',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='Categoria',
            field=models.CharField(max_length=50),
        ),
    ]
