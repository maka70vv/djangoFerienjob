from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django.db import models
from django import forms
from phonenumber_field.formfields import PhoneNumberField


# Navbar
class Navbar(models.Model):
    home = models.CharField(max_length=50)
    ferienjob = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    contacts = models.CharField(max_length=50)


# Main page
class Main(models.Model):
    # Header
    start_image = models.ImageField(upload_to="")
    company_name = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)
    # Info block 1
    b1_title = models.CharField(max_length=100)
    b1_big_text = models.TextField()
    b1_lit_text = models.TextField()
    # Info block 2
    b2_title = models.CharField(max_length=100)
    b2_big_text = models.TextField()
    b2_lit_text = models.TextField()
    feedback_title = models.CharField(max_length=100, null=True)


# Feedback cards
class Feedback(models.Model):
    student_name = models.CharField(max_length=100, null=True)
    card_image = models.ImageField(upload_to="")
    year_land = models.CharField(max_length=200)
    card_text = models.TextField()


# Ferienjob page
class Ferienjob(models.Model):
    # Header
    main_title = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)
    # Info block 1
    b1_title = models.CharField(max_length=100)
    b1_big_text = models.TextField()
    b1_lit_text = models.TextField()
    b1_image = models.ImageField(upload_to="")
    # Info block 2
    b2_title = models.CharField(max_length=100)
    b2_big_text = models.TextField()
    b2_lit_text = models.TextField()
    b2_image = models.ImageField(upload_to="")


# Deutschkurs page
class Course(models.Model):
    # Header
    main_title = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)
    # Info block 1
    b1_title = models.CharField(max_length=100)
    b1_big_text = models.TextField()
    b1_lit_text = models.TextField()
    b1_image = models.ImageField(upload_to="")
    # Info block 2
    b2_title = models.CharField(max_length=100)
    b2_big_text = models.TextField()
    b2_lit_text = models.TextField()
    b2_image = models.ImageField(upload_to="")


# Contacts page
class Contacts(models.Model):
    # Header
    main_title = models.CharField(max_length=100)
    title_form = models.CharField(max_length=100, null=True)
    small_title = models.CharField(max_length=100, null=True)
    button_form = models.CharField(max_length=100, null=True)
    # Address
    title_address = models.CharField(max_length=100)
    address = models.TextField()
    phone_num = models.CharField(max_length=13)
    mail_contacts = models.EmailField(max_length=250)
    # Map
    map_link = models.TextField()


# Form registration
class Form_page(models.Model):
    # Title
    title = models.CharField(max_length=100)
    background = models.ImageField(null=True)
    saved_text = models.TextField(null=True)
    button_text = models.CharField(max_length=100, null=True)



class Form_registr(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=13)
    age = models.IntegerField()
    mail = models.EmailField(max_length=256)
    ferienjob = models.BooleanField(null=True)
    course = models.BooleanField(null=True)
    LEVEL = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2+', 'B2+')
    )
    level = models.CharField(max_length=60, choices=LEVEL, null=True)


    def __str__(self):
        return self.first_name


class Contact_form(models.Model):
    name = models.CharField(max_length=150)
    mail = models.EmailField(max_length=256)
    theme = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name