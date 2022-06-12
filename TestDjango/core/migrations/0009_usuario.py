# Generated by Django 4.0.5 on 2022-06-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_usuario_idusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de usuario')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos')),
                ('contrasena', models.CharField(max_length=50, verbose_name='contrasena')),
            ],
        ),
    ]
