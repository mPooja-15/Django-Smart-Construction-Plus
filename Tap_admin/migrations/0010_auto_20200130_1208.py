# Generated by Django 3.0.1 on 2020-01-30 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0009_material_materialtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='material_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tap_admin.MaterialType'),
        ),
    ]
