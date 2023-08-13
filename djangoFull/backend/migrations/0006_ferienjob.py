# Generated by Django 4.2.3 on 2023-07-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_feedback_feedback_title_main_feedback_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ferienjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=100)),
                ('button_text', models.CharField(max_length=100)),
                ('b1_title', models.CharField(max_length=100)),
                ('b1_big_text', models.TextField()),
                ('b1_lit_text', models.TextField()),
                ('b1_image', models.ImageField(upload_to='')),
                ('b2_title', models.CharField(max_length=100)),
                ('b2_big_text', models.TextField()),
                ('b2_lit_text', models.TextField()),
                ('b2_image', models.ImageField(upload_to='')),
            ],
        ),
    ]