from django.urls import path
from . import views

urlpatterns = [
    path('', views.doc_upload, name = "Document Upload"),
]
