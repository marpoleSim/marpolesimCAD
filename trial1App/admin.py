from django.contrib import admin

# Register your models here.
from .models import Part, Order

admin.site.register(Part)
admin.site.register(Order)
