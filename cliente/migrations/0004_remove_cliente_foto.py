# Generated by Django 4.0.3 on 2022-06-13 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_cliente_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto',
        ),
    ]
