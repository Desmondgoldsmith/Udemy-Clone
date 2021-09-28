from django.db import models
import uuid
# Create your models here.
class courses(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated= models.DateTimeField(auto_now = True)
    # author = models.ForeignKey(user)
    language = models.CharField(max_length=60)
    course_section = models.ManyToManyField('course_section')
    comments = models.ManyToManyField('comments')
    images = models.ImageField(upload_to = 'course_images')
    course_uuid = models.UUIDField(default=uuid.uuid4,unique= True)
    price = models.DecimalField(max_digits=5,decimal_places=2)


class courseSection(models.Model):
    title = models.CharField(max_length=255)
    episodes = models.ManyToManyField('episodes') 

class episodes(models.Model):
    title = models.CharField(max_length=225)
    files = models.FileField(upload_to = 'course_videos')
    length= models.DecimalField(max_digits=10,decimal_places=2)

class comments(models.Model):
    # user =  user = models.ForeignKey(user)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class sector(models.Model):
     name= models.CharField(max_length=225)
     sector_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
     related_courses = models.ManyToManyField('Courses')
     sector_image = models.ImageField(upload_to = 'sector_image')
