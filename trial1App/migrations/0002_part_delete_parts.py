# Generated by Django 5.1.5 on 2025-01-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial1App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.BooleanField()),
                ('partName', models.CharField(default='none', max_length=30)),
                ('functionName', models.CharField(max_length=30)),
                ('arg0Name', models.CharField(max_length=30)),
                ('arg0Value', models.FloatField()),
                ('arg1Name', models.CharField(max_length=30)),
                ('arg1Value', models.FloatField(default=0)),
                ('arg2Name', models.CharField(max_length=30)),
                ('arg2Value', models.FloatField()),
                ('arg3Name', models.CharField(max_length=30)),
                ('arg3Value', models.FloatField()),
                ('arg4Name', models.CharField(max_length=30)),
                ('arg4Value', models.FloatField()),
                ('arg5Name', models.CharField(max_length=30)),
                ('arg5Value', models.FloatField()),
                ('arg6Name', models.CharField(max_length=30)),
                ('arg6Value', models.FloatField()),
                ('arg7Name', models.CharField(max_length=30)),
                ('arg7Value', models.FloatField()),
                ('arg8Name', models.CharField(max_length=30)),
                ('arg8Value', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Parts',
        ),
    ]
