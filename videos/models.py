from django.db import models
import uuid
# Create your models here.


class tax_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class retirement_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class savings_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class life_insurance_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class investment_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class estate_planning_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class long_term_care_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class medicare_video(models.Model):

    
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"link: {self.link} password: {self.password}"






