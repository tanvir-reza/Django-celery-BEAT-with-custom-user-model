from rest_framework.serializers import ModelSerializer

from .models import *


class UserEduSerializer(ModelSerializer):
    class Meta:
        model = UserEducation
        fields = '__all__'


class UserSerializer(ModelSerializer):
    education = UserEduSerializer()
    class Meta:
        model = Usermanage
        fields = '__all__'



class UserLoginResponseSerializer(ModelSerializer):
    class Meta:
        model = Usermanage
        fields = '__all__'


class BookShopSerializer(ModelSerializer):
    class Meta:
        model = PrintShop
        fields = '__all__'
        many = True


class BooksSerializer(ModelSerializer):
    print_by = BookShopSerializer(many=True)
    class Meta:
        model = Books
        fields = ['title', 'author', 'created_at_formatted', 'updated_at_formatted', 'print_by']

    