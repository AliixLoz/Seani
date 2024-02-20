# Generated by Django 5.0.2 on 2024-02-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=10, verbose_name='Abreviación')),
                ('level', models.CharField(choices=[('TSU', 'Técnico Superior Universitario'), ('Ing', 'Ingeniería'), ('Lic', 'Licenciatura'), ('M', 'Maestría')], max_length=10, verbose_name='Nivel')),
            ],
            options={
                'verbose_name': ' carrera',
                'verbose_name_plural': 'carreras',
            },
        ),
    ]
