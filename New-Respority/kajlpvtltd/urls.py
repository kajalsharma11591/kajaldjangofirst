
from django.contrib import admin
from django.urls import path,include
from . import views
from transport import urls
urlpatterns = [
    path('', include('transport.urls')),
   
]


