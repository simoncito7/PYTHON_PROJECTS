# Generated by Django 3.0.3 on 2020-05-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_BBDD', '0005_remove_causa_fecha_elev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='fecha_elev2',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Fecha de elevación (DD/MM/AA)'),
        ),
    ]