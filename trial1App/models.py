from django.db import models
from django.utils.formats import date_format

from django.contrib.auth.models import User
from django.conf import settings

#from accounts.models import CompanyInfo

# Create your models here.
class Part(models.Model):
    partName = models.CharField(max_length=30, default='none')
    company = models.ForeignKey('accounts.CompanyInfo', on_delete=models.CASCADE) 
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

       return self.partName + ', ' + self.company.company

class Order(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    company = models.ForeignKey('accounts.CompanyInfo', on_delete=models.CASCADE)
    part = models.ForeignKey('Part', on_delete=models.CASCADE)
    arg0Value = models.FloatField(default=0)
    arg1Value = models.FloatField(default=0)
    arg2Value = models.FloatField(default=0)
    arg3Value = models.FloatField(default=0)
    arg4Value = models.FloatField(default=0)
    arg5Value = models.FloatField(default=0)
    arg6Value = models.FloatField(default=0)
    arg7Value = models.FloatField(default=0)
    arg8Value = models.FloatField(default=0)

    def __str__(self):

       return self.user.username + ', ' +self.company.company + ', ' + self.part.partName + ', ' + str(self.orderDate)

