# Generated by Django 3.0.3 on 2020-05-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Causa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_causa', models.CharField(max_length=50, verbose_name='Número de causa')),
                ('expediente', models.CharField(max_length=50, verbose_name='Expediente')),
                ('caratula', models.CharField(max_length=50, verbose_name='Carátula de causa')),
                ('estado_causa', models.CharField(choices=[('curso', 'En curso'), ('elev', 'Elevada'), ('tram', 'En espera')], default='En espera', max_length=10, verbose_name='Estado de causa')),
                ('fecha', models.DateField(verbose_name='Fecha de Entrada')),
                ('fecha_elev', models.DateField(verbose_name='Fecha de elevación')),
                ('juzgado', models.CharField(max_length=50, verbose_name='Juzgado interviniente')),
                ('resp_juzgado', models.CharField(max_length=50, verbose_name='Responsable de juzgado')),
                ('tel_juzgado', models.CharField(max_length=12, verbose_name='Teléfono de juzgado')),
                ('secretaria', models.CharField(max_length=50, verbose_name='Número de secretaría')),
                ('resp_secretaria', models.CharField(max_length=50, verbose_name='Responsable de secretaría')),
                ('resp_PNA', models.CharField(max_length=50, verbose_name='Personal de PNA asignado')),
                ('observ', models.CharField(max_length=400, verbose_name='Observaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(max_length=50, verbose_name='Personal que lleva a cargo el trámite')),
                ('direc', models.CharField(max_length=50, verbose_name='Dirección del personal')),
            ],
        ),
    ]
