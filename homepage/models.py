from django.db import models

# Create your models here.

class meetings(models.Model):
    start=models.CharField(max_length=24)
    end=models.CharField(max_length=18)


    def __str__(self):
        return f"Start Time: {self.start} End Time: {self.end}"

class verifed_user(models.Model):
    verified_email=models.EmailField()

    def __str__(self):
        return self.verified_email

# class recepients(models.Model):
#     email=models.EmailField()

#     def __str__(self):
#         return self.email

# class message(models.Model):

#     subject=models.TextField()
#     information=models.TextField()

#     def __str__(self):
#         return f"{self.subject}: {self.information}"