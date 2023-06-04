from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Show(models.Model):
  name= models.CharField(max_length=100)
  genre= models.CharField(max_length=100)
  seasons= models.IntegerField()
  notes= models.TextField()
  rating= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  stillWatching= models.BooleanField()

  def __str__(self):
    return self.name
  
