# Generated by Django 4.2.3 on 2023-08-20 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_categories_remove_form_registr_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_registr',
            name='category',
            field=models.ManyToManyField(to='backend.categories'),
        ),
    ]