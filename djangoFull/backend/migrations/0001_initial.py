# Generated by Django 4.2.3 on 2023-08-22 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mail', models.EmailField(max_length=256)),
                ('theme', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=100)),
                ('title_form', models.CharField(max_length=100, null=True)),
                ('small_title', models.CharField(max_length=100, null=True)),
                ('button_form', models.CharField(max_length=100, null=True)),
                ('title_address', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone_num', models.CharField(max_length=13)),
                ('mail_contacts', models.EmailField(max_length=250)),
                ('map_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
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
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100, null=True)),
                ('card_image', models.ImageField(upload_to='')),
                ('year_land', models.CharField(max_length=200)),
                ('card_text', models.TextField()),
            ],
        ),
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
        migrations.CreateModel(
            name='Form_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('background', models.ImageField(null=True, upload_to='')),
                ('saved_text', models.TextField(null=True)),
                ('button_text', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form_registr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=13)),
                ('age', models.IntegerField()),
                ('mail', models.EmailField(max_length=256)),
                ('ferienjob', models.BooleanField(null=True)),
                ('course', models.BooleanField(null=True)),
                ('level', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2+', 'B2+')], max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_image', models.ImageField(upload_to='')),
                ('company_name', models.CharField(max_length=100)),
                ('button_text', models.CharField(max_length=100)),
                ('b1_title', models.CharField(max_length=100)),
                ('b1_big_text', models.TextField()),
                ('b1_lit_text', models.TextField()),
                ('b2_title', models.CharField(max_length=100)),
                ('b2_big_text', models.TextField()),
                ('b2_lit_text', models.TextField()),
                ('feedback_title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=50)),
                ('ferienjob', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('contacts', models.CharField(max_length=50)),
            ],
        ),
    ]
