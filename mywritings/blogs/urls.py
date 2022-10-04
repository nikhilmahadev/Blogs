

from .views import home, post, category

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', home),
    path('blogs/<slug:url>', post),
    path('category/<slug:url>',category)
]
