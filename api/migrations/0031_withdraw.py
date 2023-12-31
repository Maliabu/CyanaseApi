# Generated by Django 4.1.3 on 2023-07-13 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0030_deposit_investment_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdraw_channel', models.CharField(default='bank', max_length=200)),
                ('withdarw_amount', models.BigIntegerField(default=0)),
                ('currency', models.CharField(default='UGX', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.accounttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
