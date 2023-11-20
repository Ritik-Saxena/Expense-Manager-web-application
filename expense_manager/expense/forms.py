from django.forms import ModelForm
from .models import Expense, UserProfile

class ExpenseForm(ModelForm):
    class Meta():
        model = Expense
        fields = '__all__'
        exclude = ['user_profile', 'date_added']

class UserProfileForm(ModelForm):
    class Meta():
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        disabled = ['email']