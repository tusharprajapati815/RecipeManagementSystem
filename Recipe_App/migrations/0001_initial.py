# Generated by Django 5.0.6 on 2024-06-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=150)),
                ('recipe_img', models.ImageField(upload_to='images')),
                ('ingredients', models.TextField(max_length=300)),
                ('instructions', models.TextField(max_length=700)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Recipe',
            },
        ),
    ]