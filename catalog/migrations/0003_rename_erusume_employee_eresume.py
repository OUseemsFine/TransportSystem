# Generated by Django 4.2.15 on 2024-08-30 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_department_positions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eRusume',
            new_name='eResume',
        ),
    ]
