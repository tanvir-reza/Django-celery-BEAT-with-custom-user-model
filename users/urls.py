from django.urls import path
# import asView from views
from users.views import Login

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.getBooks, name='books'),
    path('v2/books/', views.getBooks, name='books'),
    path('printshop/<name>/',views.getAllBooksOfPrintShop, name='printshop'), 
    path('users/', views.getusers, name='users'),
    path('user/login/', Login.as_view(), name='login'),
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
]