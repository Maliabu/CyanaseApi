# Generated by Django 4.1.3 on 2023-06-10 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_nextofkin'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextofkin',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
