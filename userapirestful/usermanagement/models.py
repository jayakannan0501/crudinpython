from django.db import models

# Create your models here.

class Usertable(models.Model):
    username = models.CharField(max_length=255, unique=True, db_index= True)
    email = models.EmailField(max_length=255,  db_index= True)
    password = models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
