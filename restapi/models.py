from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length= 50)
    age =  models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name


class student(models.Model):
    id =  models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50)
    score = models.DecimalField(max_digits= 10 , decimal_places= 2)

    def __str__(self):
        return self.name