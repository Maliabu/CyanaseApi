# Generated by Django 3.2.16 on 2023-08-21 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0055_auto_20230821_0733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]
