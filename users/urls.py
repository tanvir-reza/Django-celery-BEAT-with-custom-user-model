from django.urls import path,include
# import asView from views
from users.views import Login
# import router
from rest_framework.routers import DefaultRouter
# import views


from . import views

# create router object
router = DefaultRouter()
# register BooksViewSet with router
router.register('booksView', views.BooksViewSet, basename='booksView')

urlpatterns = [
    path('', include(router.urls)),
    path('books/', views.getBooks, name='books'),
    path('books-filter/', views.bookFilter, name='books-filter'),
    path('v2/books/', views.getBooks, name='books'),
    path('printshop/<name>/',views.getAllBooksOfPrintShop, name='printshop'), 
    path('users/', views.getusers, name='users'),
    path('user/login/', Login.as_view(), name='login'),
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
]