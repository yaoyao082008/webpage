from django.db import models
import uuid
# Create your models here.


class tax_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class retirement_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class college_university_savings_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class life_insurance_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class asset_protection_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class estate_planning_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']


    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class long_term_care_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class medicare_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"

class other_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"
    

class exam_video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"
    
class Real_Estate_Investment_Video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"
    
class General_Financial_Planning_Video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"
    
class Company_Structure_Video(models.Model):

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    link=models.CharField(max_length=1000)
    password=models.CharField(max_length=40,default='N/A')
    title=models.CharField(max_length=500,default='Title')
    author=models.CharField(max_length=200,default='Anonymous')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"link: {self.link} password: {self.password}"






