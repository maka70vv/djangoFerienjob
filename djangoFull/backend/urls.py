from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("ferienjob/", views.ferienjob, name="ferienjob"),
    path("course/", views.course, name="course"),
    path("contacts/", views.contacts, name="contacts"),
    path("registrate/", views.add_form, name="form"),
    path("registrate/postform/", views.add_form, name="postform"),
    path("success/", views.success_form, name="success"),
    path("contacts/message/", views.contacts, name="contact_form")
]
