# Generated by Django 3.0.1 on 2020-03-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0020_auto_20200305_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]