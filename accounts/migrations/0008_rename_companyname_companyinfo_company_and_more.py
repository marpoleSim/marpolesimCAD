# Generated by Django 5.1.5 on 2025-01-27 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_companyinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='companyName',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='companyinfo',
            old_name='phoneNumber',
            new_name='phone',
        ),
    ]
