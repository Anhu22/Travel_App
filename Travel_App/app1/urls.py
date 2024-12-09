from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', views.login, name="login"),
    path('login1.html',views.login1),  # Changed to lowercase for consistency
    path('sign.html', views.sign, name="signup"),
    path('index/',views.index),
    path('show/',views.show),  # Changed to a more RESTful URL
    path('homepage.html', views.home, name="homepage"),  # Changed to a more RESTful URL
]