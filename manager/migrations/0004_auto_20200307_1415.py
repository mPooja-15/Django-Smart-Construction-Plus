# Generated by Django 3.0.1 on 2020-03-07 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0020_auto_20200305_1423'),
        ('manager', '0003_dailyreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tap_admin.Project'),
        ),
        migrations.AlterField(
            model_name='managerprofile',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]
