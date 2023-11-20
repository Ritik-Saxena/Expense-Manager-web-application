from django.urls import path, re_path
from . import views

app_name = 'expense'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^ExpenseID/create/$', views.createExpense, name='create_expense'),
    re_path(r'^ExpenseID/(?P<pk>\d+)/update/$', views.updateExpense, name='update_expense'),
    re_path(r'^ExpenseID/(?P<pk>\d+)/delete/$', views.deleteExpense, name='delete_expense'),
    
    re_path(r'^sort_expense/price_max_to_min/$', views.sort_expense_price_max_to_min, name='price_max_to_min'),
    re_path(r'^sort_expense/price_min_to_max/$', views.sort_expense_price_min_to_max, name='price_min_to_max'),
    re_path(r'^sort_expense/date_beginning/$', views.sort_expense_date_beginning, name='date_beginning'),
    re_path(r'^sort_expense/date_end/$', views.sort_expense_date_end, name='date_end'),

    re_path(r'^user/profile/$', views.userProfile, name="user_profile"),

    re_path(r'^about/$', views.about, name="about"),

    re_path(r'^clear_all_expense$', views.clear_all_expense, name="clear_all_expense"),

    re_path(r'^graph_analysis$', views.graph_analysis, name="graph_analysis"),


]
