from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('controlme/', admin.site.urls),
]
