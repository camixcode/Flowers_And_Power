# Generated by Django 4.0.4 on 2022-06-10 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=None, null=True, upload_to='producto'),
        ),
    ]
