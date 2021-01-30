from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from snippets import views



urlpatterns = [
    path('', include('snippets.urls')),
    path('admin/', admin.site.urls),

]