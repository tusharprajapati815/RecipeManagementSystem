# Generated by Django 5.0.6 on 2024-06-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_img',
            field=models.ImageField(upload_to=''),
        ),
    ]