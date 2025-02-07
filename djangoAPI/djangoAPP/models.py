from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    country = models.CharField(max_length=255)
    favorite_genres = models.JSONField(default=list)
    
    
