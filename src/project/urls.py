from django.contrib import admin
from django.urls import path

from project import views
from tasks.lesson03 import task301

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("tasks/3/301/", task301.handler),
]
