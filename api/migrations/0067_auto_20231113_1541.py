# Generated by Django 3.2.16 on 2023-11-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_deposit_investment_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentoption',
            old_name='unit',
            new_name='units',
        ),
        migrations.AddField(
            model_name='deposit',
            name='units',
            field=models.BigIntegerField(default=0),
        ),
    ]