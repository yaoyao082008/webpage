from django.db import models

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

    def __str__(self):
        return self.verified_email
