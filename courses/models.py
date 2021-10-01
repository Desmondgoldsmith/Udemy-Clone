from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.
User = get_user_model()

class Sector(models.Model):
    name = models.CharField(max_length=225)
    sector = models.UUIDField(default=uuid.uuid4, unique= True)
    related_courses = models.ManyToManyField('Course')
    sector_image = models.ImageField(upload_to = 'sector_image')

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated= models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,)
    language = models.CharField(max_length=60)
    course_section = models.ManyToManyField('CourseSection')
    comments = models.ManyToManyField('comments')
    images = models.ImageField(upload_to = 'course_images')
    course_uuid = models.UUIDField(default=uuid.uuid4,unique= True)
    price = models.DecimalField(max_digits=5,decimal_places=2)


class CourseSection(models.Model):
    title = models.CharField(max_length=255)
    episodes = models.ManyToManyField('Episodes') 

class Episodes(models.Model):
    title = models.CharField(max_length=225)
    files = models.FileField(upload_to = 'course_videos')
    length= models.DecimalField(max_digits=10,decimal_places=2)

class Comments(models.Model):
    user_ =  models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

# class sector(models.Model):
#      name= models.CharField(max_length=225)
#      sector_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#      related_courses = models.ManyToManyField('Courses')
#      sector_image = models.ImageField(upload_to = 'sector_image')