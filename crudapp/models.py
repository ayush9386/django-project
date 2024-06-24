from django.db import models

# Create your models here.
class user_detail(models.Model):
    name = models.CharField(max_length= 50)
    phone_num = models.IntegerField()
    no_of_people = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name