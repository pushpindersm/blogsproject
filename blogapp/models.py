from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=CloudinaryField('image')
    description=models.TextField()
    created=models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

