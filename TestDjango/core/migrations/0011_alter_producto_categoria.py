# Generated by Django 4.0.5 on 2022-06-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_producto_idproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(max_length=50, verbose_name='categoria'),
        ),
    ]
