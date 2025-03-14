# Generated by Django 5.1.5 on 2025-01-22 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial1App', '0004_rename_check_in_part_checkin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.BooleanField()),
                ('userName', models.CharField(default='none', max_length=30)),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('partName', models.CharField(default='none', max_length=30)),
                ('templateName', models.CharField(default='none', max_length=30)),
                ('numberOfArgs', models.IntegerField(default=1)),
                ('arg0Name', models.CharField(default='none', max_length=30)),
                ('arg0Value', models.FloatField(default=0)),
                ('arg1Name', models.CharField(default='none', max_length=30)),
                ('arg1Value', models.FloatField(default=0)),
                ('arg2Name', models.CharField(default='none', max_length=30)),
                ('arg2Value', models.FloatField(default=0)),
                ('arg3Name', models.CharField(default='none', max_length=30)),
                ('arg3Value', models.FloatField(default=0)),
                ('arg4Name', models.CharField(default='none', max_length=30)),
                ('arg4Value', models.FloatField(default=0)),
                ('arg5Name', models.CharField(default='none', max_length=30)),
                ('arg5Value', models.FloatField(default=0)),
                ('arg6Name', models.CharField(default='none', max_length=30)),
                ('arg6Value', models.FloatField(default=0)),
                ('arg7Name', models.CharField(default='none', max_length=30)),
                ('arg7Value', models.FloatField(default=0)),
                ('arg8Name', models.CharField(default='none', max_length=30)),
                ('arg8Value', models.FloatField(default=0)),
            ],
        ),
    ]
