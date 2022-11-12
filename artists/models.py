from enum import unique
from django.db import models
from users.models import User

# Create your models here.
class Artist (models.Model):
    stage_name=models.CharField(max_length=30,unique=True,blank=False,null=False)
    social_link= models.URLField(blank=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
