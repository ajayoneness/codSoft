from django.db import models


class Password(models.Model):
    username = models.CharField(max_length=40, null=True, blank=True)
    length = models.IntegerField(null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)