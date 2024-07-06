from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=150, null=False)
    recipe_img = models.ImageField()
    description = HTMLField(max_length=400, null=False)
    ingredients = HTMLField(max_length=2000, null=False)
    instructions = HTMLField(max_length=2000, null=False)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.recipe_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Recipe'