# Generated by Django 4.1.3 on 2023-06-12 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0024_nextofkin_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextofkin',
            name='email',
            field=models.EmailField(default='nextofkin@gmail.com', max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='nextofkin',
            name='first_name',
            field=models.CharField(default='first name', max_length=200, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='nextofkin',
            name='last_name',
            field=models.CharField(default='last name', max_length=200, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='nextofkin',
            name='phone',
            field=models.IntegerField(default='+256 000 000 000', verbose_name='phone'),
        ),
        migrations.CreateModel(
            name='Riskprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qn1', models.CharField(default='saving', max_length=200, verbose_name='objectives')),
                ('qn2', models.CharField(default='less_than_year', max_length=200, verbose_name='horizon')),
                ('qn3', models.CharField(default='treasuries', max_length=200, verbose_name='past investing')),
                ('qn4', models.CharField(default='less_ten_percent', max_length=200, verbose_name='portfolio max loss')),
                ('qn5', models.CharField(default='least', max_length=200, verbose_name='capital')),
                ('qn6', models.CharField(default='employment', max_length=200, verbose_name='funds source')),
                ('qn7', models.CharField(default='guaranteed_returns', max_length=200, verbose_name='goals')),
                ('qn8', models.CharField(default='A', max_length=200, verbose_name='profit or loss')),
                ('qn9', models.CharField(default='no', max_length=200, verbose_name='risk')),
                ('qn10', models.CharField(default='no', max_length=200, verbose_name='future investing')),
                ('qn11', models.CharField(default='comfortable', max_length=200, verbose_name='inflation impact')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
