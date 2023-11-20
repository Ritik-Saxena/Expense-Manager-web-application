from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    display_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='user_avatar')
    def __str__(self):
        return "{0} | User Profile".format(self.display_name)

class Expense(models.Model):
    CATEGORY = (
        ('Food & Drink', 'Food & Drink'),
        ('Shopping', 'Shopping'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Healthcare', 'Healthcare'),
        ('Travel', 'Travel'),
        ('Gifts', 'Gifts'),
        ('Education', 'Education'),
        ('Family & Personal', 'Family & Personal'),
        ('Bills & Fees', 'Bills & Fees'),
        ('Groceries', 'Groceries'),
        ('Beauty', 'Beauty'),
        ('Others', 'Others'),
    )
    user_profile = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30, verbose_name="Expense Title")
    price = models.FloatField(default=0)
    desc = models.TextField(max_length=200, null=True, blank=True, verbose_name="Description")
    category = models.CharField(max_length=40, choices=CATEGORY)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{0} | {1} | {2}".format(self.user_profile.display_name, self.title, self.price)
    
    def get_absolute_url(self):
        return reverse(viewname='expense:index')




    