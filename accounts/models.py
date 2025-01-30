from django.db import models

from django.contrib.auth.models import User
from django.conf import settings

class UserType(models.Model):

    isCompany = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
       if self.isCompany:
          userType = "company"
       else:
          userType = "individual"

       return self.user.username + ': ' + userType

# company info table
class CompanyInfo(models.Model):

    company = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):

        return self.company

# user info table
class UserInfo(models.Model):

    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    postCode = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username

