from collections.abc import Iterable
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class verifed_user(models.Model):
    
    verified_email=models.EmailField()
    
    def save(self):

        if not verifed_user.objects.filter(verified_email=self.verified_email):
            return super().save()
        
    def __str__(self):
        return self.verified_email
    
class everyone_video_number(models.Model):
    Tax_Video_Number=models.IntegerField(default=1)
    Long_Term_Care_Video_number=models.IntegerField(default=1)
    Retirement_Video_Number=models.IntegerField(default=1)
    Savings_Video_Number=models.IntegerField(default=1)
    Life_Insurance_Video_Number=models.IntegerField(default=1)
    Asset_Protection_Video_Number=models.IntegerField(default=1)
    Estate_Planning_Video_Number=models.IntegerField(default=1)
    Medicare_Video_Number=models.IntegerField(default=1)
    Other_Video_Number=models.IntegerField(default=1)
    Real_Estate_Investment_Video_Number=models.IntegerField(default=1)
    General_Financial_Planning_Video_Number=models.IntegerField(default=1)
    Company_Structure_Video_Number=models.IntegerField(default=1)

    def __str__(self):
        return "EVERYONES VIDEO NUMBER (do not add more)"
    
class inner_webinar(models.Model):

    title=models.CharField(max_length=200)
    description=RichTextField(blank=True,null=True)
    date=models.DateField()
    hour=models.CharField(max_length=200)
    type=models.CharField(max_length=200)

    def __str__(self):
        return str(self.date)
    
class chinese_webinar(models.Model):

    title=models.CharField(max_length=200)
    description=RichTextField(blank=True,null=True)
    date=models.DateField()
    hour=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    link=models.TextField(default='https://www.youtube.com')

    def __str__(self):
        return str(self.date)
    
class english_webinar(models.Model):

    title=models.CharField(max_length=200)
    description=RichTextField(blank=True,null=True)
    date=models.DateField()
    hour=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    link=models.TextField(default='https://www.youtube.com')

    def __str__(self):
        return str(self.date)
    
class agent_contact(models.Model):

    wechat_qrcode=models.ImageField(null=True,blank=True,upload_to='contact/pictures/' , default='contact/pictures/default.jpg')
    name=models.CharField(max_length=200)
    email=models.TextField()
    phone_number=models.CharField(max_length=200)

    def __str__(self):
        return self.name
