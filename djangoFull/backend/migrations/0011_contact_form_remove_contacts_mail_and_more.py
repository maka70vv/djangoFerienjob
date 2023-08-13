# Generated by Django 4.2.3 on 2023-08-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_contacts_small_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_form', models.CharField(max_length=100)),
                ('small_title', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=150)),
                ('mail', models.EmailField(max_length=256)),
                ('theme', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='message',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='small_title',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='title_form',
        ),
    ]
