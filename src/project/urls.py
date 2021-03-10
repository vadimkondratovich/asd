from django.contrib import admin
from django.urls import path
from django.urls import include

from project import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("tasks/103/", include("applications.task103.urls")),
    path("tasks/301/", include("applications.task301.urls")),
    path("tasks/302/", include("applications.task302.urls")),
    path("tasks/303/", include("applications.task303.urls")),
    path("tasks/304/", include("applications.task304.urls")),
    path("tasks/305/", include("applications.task305.urls")),
    path("tasks/402/", include("applications.task402.urls")),
]
