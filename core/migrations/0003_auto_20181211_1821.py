# Generated by Django 2.1.3 on 2018-12-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181211_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='delivered_at',
            field=models.DateTimeField(blank=True, verbose_name='Teslim tarihi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='repaired_at',
            field=models.DateTimeField(blank=True, verbose_name='Onarılma tarihi'),
        ),
    ]