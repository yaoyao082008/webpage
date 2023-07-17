from django.db import models

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    body=models.TextField()
    image=models.ImageField(null=True,blank=True,upload_to='blog/pictures/' , default='blog/pictures/default.jpg')
    def __str__(self):
        return f"{self.title} | {self.first_name} {self.last_name}"