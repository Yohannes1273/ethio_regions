
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('create_regions/', views.create_region, name="create_regions"),
]
