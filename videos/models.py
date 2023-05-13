from django.db import models

# Create your models here.


class tax_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class retirement_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class savings_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class life_insurance_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class investment_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class estate_planning_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class long_term_care_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class medicare_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')

    def __str__(self):
        return f"link: {self.link} password: {self.password}"






