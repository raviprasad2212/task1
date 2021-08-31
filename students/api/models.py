from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=200)
    rollnumber = models.CharField(max_length=200, unique=True)
    dateofbirth = models.DateField()

    def __str__(self):
        return self.name