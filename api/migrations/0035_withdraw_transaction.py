# Generated by Django 4.1.3 on 2023-07-19 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_banktransactions_deposit_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.banktransactions'),
            preserve_default=False,
        ),
    ]
