# Generated by Django 3.0.1 on 2020-01-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerprofile',
            name='pincode',
            field=models.IntegerField(default=395010),
        ),
    ]
