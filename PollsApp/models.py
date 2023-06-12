from django.db import models


class User_prova(models.Model):
    username = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)

