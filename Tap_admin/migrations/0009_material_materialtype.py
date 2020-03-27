# Generated by Django 3.0.1 on 2020-01-25 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0008_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('purchased_date', models.DateField()),
                ('company_name', models.CharField(max_length=100)),
                ('material_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tap_admin.MaterialType')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tap_admin.Project')),
            ],
        ),
    ]
