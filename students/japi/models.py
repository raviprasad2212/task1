from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=200)
    rollnumber = models.CharField(max_length=200, unique=True)
    dateofbirth = models.DateField()

    def __str__(self):
        return self.name
    
class StudentMarks(models.Model):
    rollnumber = models.OneToOneField(Students, on_delete=CASCADE)
    marks = models.CharField(max_length=100)