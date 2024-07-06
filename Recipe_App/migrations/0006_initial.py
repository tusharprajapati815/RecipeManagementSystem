# Generated by Django 5.0.6 on 2024-06-25 05:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Recipe_App', '0005_delete_recipe'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=150)),
                ('recipe_img', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=400)),
                ('ingredients', models.TextField(max_length=500)),
                ('instructions', models.TextField(max_length=700)),
                ('category', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Recipe',
            },
        ),
    ]