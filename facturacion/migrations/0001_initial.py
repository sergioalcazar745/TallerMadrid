# Generated by Django 4.0.3 on 2022-05-31 16:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehiculo', '0005_alter_arreglo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('concepto', models.CharField(max_length=50, null=True)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('arreglo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.arreglo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
