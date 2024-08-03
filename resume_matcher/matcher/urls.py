# resume_matcher/urls.py

from django.contrib import admin
from django.urls import path
from . import views  # Ensure you import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]


