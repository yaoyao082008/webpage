from django.db import models

# Create your models here.

class meetings(models.Model):
    start=models.CharField(max_length=24)
    end=models.CharField(max_length=18)


    def __str__(self):
        return f"Start Time: {self.start} End Time: {self.end}"

class verifed_user(models.Model):
    verified_email=models.EmailField()
    
    tax_video_number=models.IntegerField()
    long_term_care_video_number=models.IntegerField()
    retirement_video_number=models.IntegerField()
    savings_video_number=models.IntegerField()
    life_insurance_video_number=models.IntegerField()
    investment_video_number=models.IntegerField()
    estate_planning_video_number=models.IntegerField()
    medicare_video_number=models.IntegerField()

    def __str__(self):
        return self.verified_email
