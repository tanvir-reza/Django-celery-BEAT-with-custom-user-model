from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .Serializers import *
from .models import Usermanage,Books
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .filters import BookByUserFilter
from rest_framework.pagination import PageNumberPagination



# Create your views here.
@api_view(['GET'])
def home(request):

    return Response({"message": "Hello, world!"})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getusers(request):
    queryset = Usermanage.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBooks(request):
    userD = request.user
    queryset = userD.books.all()
    serializer = BooksSerializer(queryset, many=True)

    return Response(serializer.data)


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    def get_queryset(self):
        return Books.objects.all()
    
    def get_serializer_class(self):
        return BooksSerializer
    
    # update book details
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllBooksOfPrintShop(request):
    queryset = PrintShop.publishers.all()
    serializer = BooksSerializer(queryset, many=True)

    return Response(serializer.data)

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = Usermanage.objects.get(username=username)
        if user.is_active:
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                login_user_response = UserLoginResponseSerializer(user,context={'request': request})
                print(token.key)
                return Response({
                    "id": login_user_response.data['id'],
                    "username": login_user_response.data['username'],
                    "email": login_user_response.data['email'],
                    "token": token.key

                },status=status.HTTP_200_OK)
            else:
                return Response({"error": "Wrong password", "status": status.HTTP_400_BAD_REQUEST})
            

class UserRegistrationView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        
        if Usermanage.objects.filter(username=username).exists():
            return Response({"error": "Username already exists", "status": status.HTTP_400_BAD_REQUEST})
        else:
            user = Usermanage.objects.create_user(username=username, password=password)
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            login_user_response = UserLoginResponseSerializer(user,context={'request': request})
            return Response({
                "id": login_user_response.data['id'],
                "username": login_user_response.data['username'],
                "email": login_user_response.data['email'],
                "token": token.key
            },status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def bookFilter(request):
    queryset = Books.objects.prefetch_related('books')

    filter = BookByUserFilter(request.GET, queryset=queryset)
    serializer = BooksSerializer(filter.qs, many=True)
    return Response(serializer.data)
