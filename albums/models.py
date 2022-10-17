from django.db import models
from datetime import date,datetime
from model_utils.fields import AutoCreatedField
from django.utils.translation import gettext_lazy as _
from artists.models import Artist



# Create your models here.
class TimeStampedModel(models.Model):
    
    creation_time = AutoCreatedField(_('creation_time'))

    class Meta:
        abstract = True
 


class Album (TimeStampedModel):

    artist=models.ForeignKey(Artist, on_delete=models.CASCADE)  
    album_name=models.CharField(max_length=30,default='New Album',)
    release_time=models.DateField(blank=False)
    cost=models.FloatField(default=0)
    is_approved=models.BooleanField(default=False)
    

    def __str__(self):
        return self.album_name