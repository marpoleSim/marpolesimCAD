# Generated by Django 5.1.5 on 2025-01-27 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_usertype_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='username',
        ),
    ]
