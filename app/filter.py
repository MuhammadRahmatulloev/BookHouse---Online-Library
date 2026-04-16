import django_filters
from .models import Book, Author, Category, Publisher

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Название')

    price = django_filters.NumberFilter(field_name='price', label='Price')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Price from')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Price from')
    
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    publisher = django_filters.ModelChoiceFilter(queryset=Publisher.objects.all())
    
    class Meta:
        model = Book
        fields = ['title']