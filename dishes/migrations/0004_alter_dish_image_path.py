# Generated by Django 5.0.3 on 2024-03-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_alter_dish_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image_path',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
