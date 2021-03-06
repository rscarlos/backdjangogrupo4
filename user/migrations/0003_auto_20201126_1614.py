# Generated by Django 3.1.3 on 2020-11-26 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201124_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccionmodel',
            name='estado',
            field=models.BooleanField(db_column='estado', default=True),
        ),
        migrations.AlterField(
            model_name='usuariomodel',
            name='usuApellido',
            field=models.CharField(db_column='usu_apellido', default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usuariomodel',
            name='usuCel',
            field=models.CharField(db_column='usu_cel', default='', max_length=13),
        ),
        migrations.AlterField(
            model_name='usuariomodel',
            name='usuDni',
            field=models.CharField(db_column='usu_dni', default='', max_length=50),
        ),
    ]
