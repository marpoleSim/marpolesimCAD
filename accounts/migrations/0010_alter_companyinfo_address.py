# Generated by Django 5.1.5 on 2025-01-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_companyinfo_address_alter_companyinfo_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='address',
            field=models.CharField(max_length=60),
        ),
    ]
