from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class verifed_user(models.Model):
    verified_email=models.EmailField()
    
    tax_video_number=models.IntegerField(default=1)
    long_term_care_video_number=models.IntegerField(default=1)
    retirement_video_number=models.IntegerField(default=1)
    savings_video_number=models.IntegerField(default=1)
    life_insurance_video_number=models.IntegerField(default=1)
    investment_video_number=models.IntegerField(default=1)
    estate_planning_video_number=models.IntegerField(default=1)
    medicare_video_number=models.IntegerField(default=1)
    other_video_number=models.IntegerField(default=1)

    def __str__(self):
        return self.verified_email

    
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
