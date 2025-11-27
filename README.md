# Ex01 Django ORM Web Application
## Date: 26.11.2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM

```
admin.py

from django.contrib import admin
from .models import product,productAdmin
admin.site.register(product,productAdmin)

models.py

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

```

## OUTPUT

![alt text](<diveshwebexp1/Screenshot 2025-11-26 211726.png>)

## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
