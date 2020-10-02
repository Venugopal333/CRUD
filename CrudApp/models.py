from django.db import models

# Create your models here.
class Student(models.Model):
    Id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),

    No = models.IntegerField(unique=True)
    Name = models.CharField(max_length=64)
    Marks = models.IntegerField()
    Address = models.CharField(max_length=256)