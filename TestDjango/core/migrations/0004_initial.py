# Generated by Django 4.0.5 on 2022-06-06 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('descripcionProducto', models.CharField(max_length=50, verbose_name='Descripcion del producto')),
                ('precioProducto', models.IntegerField(verbose_name='Precio del producto')),
                ('imagen', models.FileField(upload_to='', verbose_name='Imagen producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
