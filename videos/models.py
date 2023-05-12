from django.db import models

# Create your models here.


class videos(models.Model):
    CHOICE=(('tax','Taxes'),('insurance','life insurance'))
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40)
    video_type=models.TextField(choices=CHOICE,default='tax')


    def __str__(self):
        return f"type: {self.video_type} link: {self.link} password: {self.password}"