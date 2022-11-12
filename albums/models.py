from distutils import extension
from email.policy import default
from wsgiref.validate import validator
from django.db import models
from datetime import date,datetime
from model_utils.fields import AutoCreatedField
from django.utils.translation import gettext_lazy as _
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError





# Create your models here.

class TimeStampedModel(models.Model):
    
    creation_time = AutoCreatedField(_('creation_time'))

    class Meta:
        abstract = True
 
class AlbumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)

class Album (TimeStampedModel):

    artist=models.ForeignKey(Artist, on_delete=models.CASCADE)  
    album_name=models.CharField(max_length=30,default='New Album',)
    release_time=models.DateField(blank=False)
    cost=models.FloatField(default=0)
    is_approved=models.BooleanField(default=False)

    objects = models.Manager() # The default manager.
    approved_objects = AlbumManager()
    
    def __str__(self):
        return self.album_name

# For Validation of extension of audio file:

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3','.wav']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')


class Song (models.Model):

    name = models.CharField(max_length=60 ,blank=True)
    img= models.ImageField(upload_to='',null=True,blank=True  )
    img_thumbnail=ImageSpecField(source='img' ,format='JPEG',processors=[ResizeToFill(200,100)])
    audio=models.FileField(upload_to='audio',validators=[validate_file_extension],null=True , blank=True)
    album=models.ForeignKey(Album , on_delete=models.CASCADE, )
    
    
    def __str__(self):
        return self.name