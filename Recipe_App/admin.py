from django.contrib import admin
from Recipe_App.models import Recipe

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe_name', 'category', 'user']
    list_filter = ('category', 'user')

admin.site.register(Recipe, RecipeAdmin)