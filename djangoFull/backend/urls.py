from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("ferienjob/", views.ferienjob, name="ferienjob"),
    path("course/", views.course, name="course"),
    path("contacts/", views.contacts, name="contacts")
]
