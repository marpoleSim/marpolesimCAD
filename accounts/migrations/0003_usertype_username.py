# Generated by Django 5.1.5 on 2025-01-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_userinfo_customerinfo_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='username',
            field=models.CharField(default='dd', max_length=20),
            preserve_default=False,
        ),
    ]
