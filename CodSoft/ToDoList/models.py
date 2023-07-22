from django.db import models



class taskList(models.Model):
    task = models.TextField(null=True,blank=True)