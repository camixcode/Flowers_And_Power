# Generated by Django 4.0.4 on 2022-06-13 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_producto_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='categoria_id',
        ),
    ]
