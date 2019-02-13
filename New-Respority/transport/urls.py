
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage,name='homepage'),
    path('about/', views.about),
    path('con/', views.contact),
    path('dwn/', views.downloading),
]


