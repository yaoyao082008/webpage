from django.db import models
# Create your models here.

class meetings(models.Model):
    start=models.CharField(max_length=24)
    end=models.CharField(max_length=18)


    def __str__(self):
        return f"Start Time: {self.start} End Time: {self.end}"

class verifed_user(models.Model):
    verified_email=models.EmailField()
    video_number=models.IntegerField()
    def __str__(self):
        return self.verified_email


VIDEO_CHOICES=(('tax','Taxes'),('saving','College/University Savings'),('retirement','Retirement Plans'),('life_insurance','Life Insurance'),
    ('investment','Investment'),('estate_planning','Estate Planning'),('long_term_care','Long Term Care'),('medicare','Medicare'))

class video(models.Model):
    link=models.TextField()
    password=models.TextField()
    vid_type=models.CharField(max_length=100,choices=VIDEO_CHOICES,default='Taxes')
    
    def __str__(self):

        return f"video link: {self.link} Password:{self.password}"