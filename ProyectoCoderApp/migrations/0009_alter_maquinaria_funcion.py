# Generated by Django 4.0.5 on 2022-07-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0008_herramientas_maquinaria_rename_profesor_operario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='funcion',
            field=models.CharField(max_length=30),
        ),
    ]
