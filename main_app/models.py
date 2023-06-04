from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

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
  
  def get_absolute_url(self):
      return reverse("show-detail", kwargs={"show_id": self.id})
  
  
