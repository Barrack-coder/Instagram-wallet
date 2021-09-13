from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
        author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
        image = models.ImageField(blank=True,null=True)
        captions = models.TextField()
        Created_date = models.DateField(default=timezone.now)
