from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('', views.list_voitures, name='i'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('car/<int:pk>/',CarDetail.as_view(),name = "cardetail"),
    path('list', views.index, name='list'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('login1', views.login_view, name='login1'),
    path('carsingle', views.carsingle, name='carsingle'),
    path('profil', views.profil, name='profil'),
    path('orders', views.orders, name='orders'),
    path('about', views.about, name='about'),
    path('carlist', views.carlist, name='carlist'),
    path('booking', views.booking, name='booking'),
    path('register', views.register, name='register'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('cars', views.Cars, name='cars'),
    path('addreservation', views.add_reservation, name='addreservation'),
    path('update/<int:pk>/', views.client1_update, name='update'),
]