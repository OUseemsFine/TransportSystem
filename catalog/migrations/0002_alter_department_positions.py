# Generated by Django 4.2.15 on 2024-08-30 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='positions',
            field=models.ManyToManyField(blank=True, help_text='Select a position for this department', to='catalog.position'),
        ),
    ]
