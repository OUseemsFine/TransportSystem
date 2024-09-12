# Generated by Django 4.2.15 on 2024-09-11 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_station_sname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationsequence',
            name='busline',
            field=models.ForeignKey(help_text='select a busline', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.busline'),
        ),
        migrations.AlterField(
            model_name='stationsequence',
            name='station',
            field=models.ForeignKey(help_text='select a staion', on_delete=django.db.models.deletion.CASCADE, to='catalog.station'),
        ),
    ]
