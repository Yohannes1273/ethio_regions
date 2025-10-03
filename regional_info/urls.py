
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('create_regions/', views.create_region, name="create_regions"),
    path('detail/<int:pk>', views.detail_region, name="detail"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('register/', views.register, name="register"),
    
]
