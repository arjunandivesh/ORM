from django.db import models
from django.contrib import admin
class product(models.Model):
    productId=models.CharField(primary_key=True,max_length=7)
    Name=models.CharField(max_length=30)
    Date_of_manufacturing=models.DateTimeField()
    expire_date=models.DateTimeField()
    rate=models.IntegerField()
    quantity=models.IntegerField()
    about_the_product=models.CharField(max_length=100)


class productAdmin(admin.ModelAdmin):
    list_display=["productId","Name","Date_of_manufacturing","expire_date","rate","quantity","about_the_product"]
