# Generated by Django 2.1.4 on 2018-12-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycustomusers', '0006_auto_20181223_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Admin'), (1, 'Müşteri Temsilcisi'), (2, 'Teknik Servis Görevlisi')], verbose_name='Hesap Türü'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_activated',
            field=models.DateTimeField(null=True, verbose_name='Son Aktif Edilme Tarihi'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_deactivated',
            field=models.DateTimeField(null=True, verbose_name='Son Pasif Edilme Tarihi'),
        ),
    ]