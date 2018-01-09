from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128, default='user')
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)
