from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')


class post(models.Model):
        author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
        image = models.ImageField(blank=True,null=True)
        caption = models.TextField()
        Created_date = models.DateField(default=timezone.now)
        
def __str__(self) -> str:
	return self.caption
