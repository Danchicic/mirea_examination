# Generated by Django 5.0.3 on 2024-03-21 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0013_alter_process_description_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='process_description',
            old_name='dish_id',
            new_name='dish',
        ),
    ]
