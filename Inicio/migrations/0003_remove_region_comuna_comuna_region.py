# Generated by Django 4.2.20 on 2025-05-08 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0002_alter_tipoprod_nombretipoprod_alter_venta_fechaventa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='comuna',
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inicio.region'),
            preserve_default=False,
        ),
    ]
