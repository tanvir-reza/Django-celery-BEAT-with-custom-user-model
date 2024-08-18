
from django_filters import rest_framework as filters
from .models import *


class BookByUserFilter(filters.FilterSet):
    title = filters.CharFilter(method='filter')
    print_by = filters.CharFilter(method='filter')



    class Meta:
        model = Books
        fields = ['id', 'title', 'print_by']

    
    @staticmethod
    def filter(self, queryset, name, value):
        if name == 'title':
            return queryset.filter(title=value)
        elif name == 'print_by':
            return queryset.filter(print_by=value)
        

