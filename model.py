from django.db import models

class data(models.Model):
    identity =models.CharField(max_length=100)
    pw = model.CharField(max_length=100)
