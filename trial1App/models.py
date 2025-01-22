from django.db import models
from django.utils.formats import date_format

# Create your models here.

class Part(models.Model):
    checkin = models.BooleanField()
    partName = models.CharField(max_length=30, default='none')
    functionName = models.CharField(max_length=30, default = 'none')
    numberOfArgs = models.IntegerField(default=0)
    arg0Name = models.CharField(max_length=30, default = 'none')
    arg0Value = models.FloatField(default=0)
    arg1Name = models.CharField(max_length=30, default = 'none')
    arg1Value = models.FloatField(default=0)
    arg2Name = models.CharField(max_length=30, default = 'none')
    arg2Value = models.FloatField(default=0)
    arg3Name = models.CharField(max_length=30, default = 'none')
    arg3Value = models.FloatField(default=0)
    arg4Name = models.CharField(max_length=30, default = 'none')
    arg4Value = models.FloatField(default=0)
    arg5Name = models.CharField(max_length=30, default = 'none')
    arg5Value = models.FloatField(default=0)
    arg6Name = models.CharField(max_length=30, default = 'none')
    arg6Value = models.FloatField(default=0)
    arg7Name = models.CharField(max_length=30, default = 'none')
    arg7Value = models.FloatField(default=0)
    arg8Name = models.CharField(max_length=30, default = 'none')
    arg8Value = models.FloatField(default=0)

    def __str__(self):

       return self.partName 

class Order(models.Model):
    checkin = models.BooleanField(default=False)
    userName = models.CharField(max_length=30, default = 'none')
    orderDate = models.DateField(auto_now_add=True)
    partName = models.CharField(max_length=30, default='none')
    templateName = models.CharField(max_length=30, default='none')
    numberOfArgs = models.IntegerField(default=0)
    arg0Name = models.CharField(max_length=30, default = 'none')
    arg0Value = models.FloatField(default=0)
    arg1Name = models.CharField(max_length=30, default = 'none')
    arg1Value = models.FloatField(default=0)
    arg2Name = models.CharField(max_length=30, default = 'none')
    arg2Value = models.FloatField(default=0)
    arg3Name = models.CharField(max_length=30, default = 'none')
    arg3Value = models.FloatField(default=0)
    arg4Name = models.CharField(max_length=30, default = 'none')
    arg4Value = models.FloatField(default=0)
    arg5Name = models.CharField(max_length=30, default = 'none')
    arg5Value = models.FloatField(default=0)
    arg6Name = models.CharField(max_length=30, default = 'none')
    arg6Value = models.FloatField(default=0)
    arg7Name = models.CharField(max_length=30, default = 'none')
    arg7Value = models.FloatField(default=0)
    arg8Name = models.CharField(max_length=30, default = 'none')
    arg8Value = models.FloatField(default=0)

    def __str__(self):

       return self.userName + ', ' + self.partName + ', ' + date_format(self.orderDate)

