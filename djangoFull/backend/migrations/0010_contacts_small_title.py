# Generated by Django 4.2.3 on 2023-08-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='small_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]