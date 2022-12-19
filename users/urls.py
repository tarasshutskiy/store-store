from django.urls import path
from .views import login, register, profile, cart, logout_user

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('cart/', cart, name='cart'),

]
