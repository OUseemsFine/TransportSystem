# Generated by Django 4.2.15 on 2024-09-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_vehicleinstance_platenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinstance',
            name='plateNumber',
            field=models.CharField(default='渝F13383', max_length=200, primary_key=True, serialize=False),
        ),
    ]
