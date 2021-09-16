from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    profile_pic = models.ImageField(blank=True,null=True)
    bio = models.TextField(blank=True, null=True)
    
    # title field
    # title = models.CharField(max_length=100)
    #image field
    # image = CloudinaryField('image')


class Post(models.Model):
        author = models.ForeignKey(User,on_delete=models.CASCADE)
        image = models.ImageField(blank=True,null=True)
        caption = models.TextField(blank=True, null=True)
        Created_date = models.DateField(default=timezone.now)
        comment = models.TextField(blank=True, null=True)
        like = models.ManyToManyField(User, blank=True,related_name='likes')
        
def __str__(self) -> str:
	return self.caption
