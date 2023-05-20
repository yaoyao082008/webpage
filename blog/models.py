from django.db import models

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=255)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self):
        return f"{self.title} | {self.first_name} {self.last_name}"