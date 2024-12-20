from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', views.login, name="login"),
    path('login1.html',views.login1),  # Changed to lowercase for consistency
    path('sign.html', views.sign, name="signup"),
    path('homepage.html', views.home, name="homepage"), 
    path('Messages.html',views.message, name="Message"),
    path('booking.html',views.booking,name="Booking Page"),
    path('blog.html',views.blog,name = "Blog"),
    path('package.html',views.pack,name = "Package"),
    path('search.html',views.search,name = "Search"),
    path('hotels.html',views.hotel,name="hotel"),
    path('flight.html',views.flight,name="Flight"),
    path('trains.html',views.train,name="Train"),
    path('book.html',views.book, name = "Book"),
    path('payment.html',views.pay)
]