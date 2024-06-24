from django.db import models

# Create your models here.

# Base model with common fields
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
 
    class Meta:
        abstract = True  # This model will not be used to create any database table

# Child model that inherits from CommonInfo
class Student(CommonInfo):
    major = models.CharField(max_length=100)
    class Meta(CommonInfo.Meta):
        db_table = 'student_info' # creating the db table with this name 



 
# declaring a Student Model 
SEMESTER_CHOICES = ( 
    ("1", "Civil"), 
    ("2", "Electrical"), 
    ("3", "Mechanical"), 
    ("4", "CompSci"), 
) 
class UniversityStudent(models.Model): 
      semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = '1' 
        ) 

#using this for ModelForm
class Logger(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    time_log= models.TimeField( help_text= 'enter the exact time')


class Reservation(models.Model):
    name = models.CharField(max_length= 50)
    contact = models.CharField('phone number',max_length= 50)
    time  = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    

class Person(models.Model):
    last_name  = models.TextField()
    first_name = models.TextField()

    # def __str__(self): 
    #     return f"{self.last_name}, {self.first_name}" 
    
class Employees(models.Model):
    last_name  = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50)
    shift = models.IntegerField(max_length = 50)

    def __str__(self):
        return self.first_name
    
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self):
        return self.name