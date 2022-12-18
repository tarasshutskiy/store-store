from django.urls import path
from .views import login, register, profile, cart

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('cart/', cart, name='cart'),

]
