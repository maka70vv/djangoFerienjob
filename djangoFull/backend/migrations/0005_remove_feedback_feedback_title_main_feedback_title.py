# Generated by Django 4.2.3 on 2023-07-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_feedback_remove_main_card_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_title',
        ),
        migrations.AddField(
            model_name='main',
            name='feedback_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]