from django.db import models
from unicodedata import name
# Create your models here.
class Menu(models.Model):
    food_name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()
    #category = models.CharField(max_length = 50 )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' : ' + self.cuisine
    
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length = 200)
    
class Drinks(models.Model):
    drink = models.CharField(max_length = 200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete = models.PROTECT,default = None)

    