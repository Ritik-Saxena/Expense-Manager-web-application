import django_filters
from django_filters import CharFilter, NumberFilter, DateFilter
from .models import Expense

class ExpenseFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Expense')
    price_gte = NumberFilter(field_name='price', lookup_expr='gte', label='Price (greater equal to)')
    price_lte = NumberFilter(field_name='price', lookup_expr='lte', label='Price (less equal to)')
    date_gte = DateFilter(field_name='date_added', lookup_expr='gte', label='From date (MM/DD/YYYY)')
    date_lte = DateFilter(field_name='date_added', lookup_expr='lte', label='Before date (MM/DD/YYYY)')
    desc = CharFilter(field_name='desc', lookup_expr='icontains', label='Description')
    
    class Meta():
        model = Expense
        fields = ['category']
        exclude = ['title', 'price', 'desc', 'date_added']

