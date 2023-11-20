from django.shortcuts import render, redirect
from .models import Expense, UserProfile
from .fusioncharts import FusionCharts
from .filters import ExpenseFilter
from .forms import ExpenseForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime
from collections import OrderedDict

# chart execution
def pie_chart(expense_list):
    # chart data
    category_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for expense in expense_list:
        if (expense.category == 'Food & Drink'):
            category_list[0] += expense.price
        elif (expense.category == 'Shopping'):
            category_list[1] += expense.price
        elif (expense.category == 'Transport'):
            category_list[2] += expense.price
        elif (expense.category == 'Entertainment'):
            category_list[3] += expense.price
        elif (expense.category == 'Healthcare'):
            category_list[4] += expense.price
        elif (expense.category == 'Travel'):
            category_list[5] += expense.price
        elif (expense.category == 'Gifts'):
            category_list[6] += expense.price
        elif (expense.category == 'Education'):
            category_list[7] += expense.price
        elif (expense.category == 'Family & Personal'):
            category_list[8] += expense.price
        elif (expense.category == 'Bills & Fees'):
            category_list[9] += expense.price
        elif (expense.category == 'Groceries'):
            category_list[10] += expense.price
        elif (expense.category == 'Beauty'):
            category_list[11] += expense.price
        elif (expense.category == 'Others'):
            category_list[12] += expense.price
        

    # Fusioncharts: Pie Chart
    chartObj = FusionCharts( 'pie3d', 'ex1', '75%', '60%', 'chart-1', 'json', {
            "chart": {
                "caption": "Expenditure Chart",
                "subcaption": "All Time",
                "showvalues": "1",
                "showpercentintooltip": "0",
                "numberprefix": "Rs ",
                "enablemultislicing": "1",
                "theme": "fusion",
                "exportEnabled": "1",
                "showBorder": "1",
                "borderThickness": "3",
                "borderColor": "#343a40",
                "borderAlpha": "20",
                "bgcolor": "#fbfcfd",
            },
            "data": [
                {
                "label": "Food & Drink",
                "value": category_list[0]
                },
                {
                "label": "Shopping",
                "value": category_list[1]
                },
                {
                "label": "Transport",
                "value": category_list[2]
                },
                {
                "label": "Entertainment",
                "value": category_list[3]
                },
                {
                "label": "Healthcare",
                "value": category_list[4]
                },
                {
                "label": "Travel",
                "value": category_list[5]
                },
                {
                "label": "Gifts",
                "value": category_list[6]
                },
                {
                "label": "Education",
                "value": category_list[7]
                },
                {
                "label": "Family & Personal",
                "value": category_list[8]
                },
                {
                "label": "Bills & Fees",
                "value": category_list[9]
                },
                {
                "label": "Groceries",
                "value": category_list[10]
                },
                {
                "label": "Beauty",
                "value": category_list[11]
                },
                {
                "label": "Others",
                "value": category_list[12]
                },
            ]
        })
    
    if len(expense_list) == 0:          # added login in index() function also
        chartObj = None

    return expense_list, category_list, chartObj



# django filter
def search(request, expense_list):
    expense_filter = ExpenseFilter(data=request.GET, queryset=expense_list)
    expense_list = expense_filter.qs
    # if (expense_list == None):
    #     expense_list = "No search found. Please try another one."
    total = 0
    for expense in expense_list:
        total += expense.price
    
    return total, expense_filter, expense_list



# Sorting expense_list
@login_required(login_url='user_login', redirect_field_name=None)
def sort_expense_price_max_to_min(request):
    expense_list = request.user.userprofile.expense_set.all().order_by("-price")
    
    total = 0
    for expense in expense_list:
        total += expense.price
    
    # search
    if (request.method=="GET"):
        total, expense_filter, expense_list = search(request=request, expense_list=expense_list)

    expense_list, category_list, chartObj = pie_chart(expense_list=expense_list)

    
    context = {
    'expense_list': expense_list,
    'total': total,
    'pie_chart': chartObj.render(),
    'category_list': category_list,
    'expense_filter': expense_filter,
    }

    return render(request=request, template_name='expense/index.html', context=context)


@login_required(login_url='user_login', redirect_field_name=None)
def sort_expense_price_min_to_max(request):
    expense_list = request.user.userprofile.expense_set.all().order_by("price")
    
    total = 0
    for expense in expense_list:
        total += expense.price
    
    # search
    if (request.method=="GET"):
        total, expense_filter, expense_list = search(request=request, expense_list=expense_list)

    # pie chart
    expense_list, category_list, chartObj = pie_chart(expense_list=expense_list)

    
    context = {
    'expense_list': expense_list,
    'total': total,
    'pie_chart': chartObj.render(),
    'category_list': category_list,
    'expense_filter': expense_filter,
    }

    return render(request=request, template_name='expense/index.html', context=context)


@login_required(login_url='user_login', redirect_field_name=None)
def sort_expense_date_beginning(request):
    expense_list = request.user.userprofile.expense_set.all().order_by("date_added")
    
    total = 0
    for expense in expense_list:
        total += expense.price
    
    # search
    if (request.method=="GET"):
        total, expense_filter, expense_list = search(request=request, expense_list=expense_list)

    expense_list, category_list, chartObj = pie_chart(expense_list=expense_list)

    
    context = {
    'expense_list': expense_list,
    'total': total,
    'pie_chart': chartObj.render(),
    'category_list': category_list,
    'expense_filter': expense_filter,
    }

    return render(request=request, template_name='expense/index.html', context=context)



@login_required(login_url='user_login', redirect_field_name=None)
def sort_expense_date_end(request):
    expense_list = request.user.userprofile.expense_set.all().order_by("-date_added")
    
    total = 0
    for expense in expense_list:
        total += expense.price
    
    # search
    if (request.method=="GET"):
        total, expense_filter, expense_list = search(request=request, expense_list=expense_list)

    expense_list, category_list, chartObj = pie_chart(expense_list=expense_list)

    
    context = {
    'expense_list': expense_list,
    'total': total,
    'pie_chart': chartObj.render(),
    'category_list': category_list,
    'expense_filter': expense_filter,
    }

    return render(request=request, template_name='expense/index.html', context=context)



# List view, Filter, Chart
@login_required(login_url='user_login', redirect_field_name=None)
def index(request):
    expense_list = request.user.userprofile.expense_set.all().order_by("-date_added")           # check

    total = 0
    for expense in expense_list:
        total += expense.price
    
    # search
    if (request.method=="GET"):
        total, expense_filter, expense_list = search(request=request, expense_list=expense_list)

    # calling chart function
    expense_list, category_list, chartObj = pie_chart(expense_list=expense_list)


    if (chartObj == None):          # logic to print message if no data is available to display chart
        pie_chart_obj = None
    else:
        pie_chart_obj = chartObj.render()
    
    context = {
        'expense_list': expense_list,
        'total': "{:.2f}".format(total),
        'pie_chart': pie_chart_obj,
        'category_list': category_list,
        'expense_filter': expense_filter,
    }
    
    return render(request=request, template_name='expense/index.html', context=context)


# Create, update, delete expense
@login_required(login_url='user_login', redirect_field_name=None)
def  createExpense(request):
    form = ExpenseForm()

    if (request.method=="POST"):
        form = ExpenseForm(data=request.POST)
        if (form.is_valid()):
            # expense_obj = form.save()
            Expense.objects.create(
                user_profile=request.user.userprofile,
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                desc=form.cleaned_data.get('desc'),
                category=form.cleaned_data.get('category'),
            )
            return redirect(to='expense:index')

    context = {'form': form}
    return render(request=request, template_name='expense/expense_form.html', context=context)


@login_required(login_url='user_login', redirect_field_name=None)
def updateExpense(request, pk):
    expense_obj = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=expense_obj)
    context = {'form':form}
    # print(request.user.userprofile.expense_set.get(id=pk))            # check
    # print(expense.userprofile.objects.get(user_profile=))

    if (request.method=="POST"):
        form = ExpenseForm(data=request.POST, instance=expense_obj)
        if (form.is_valid()):
            form.save()
            return redirect(to='expense:index')
    return render(request=request, template_name='expense/expense_form.html', context=context)


@login_required(login_url='user_login', redirect_field_name=None)
def deleteExpense(request, pk):
    expense_obj = Expense.objects.get(id=pk)
    expense_obj.delete()
    
    return redirect(to='expense:index')


@login_required(login_url='user_login', redirect_field_name=None)
def userProfile(request):
    form = UserProfileForm(instance=request.user.userprofile)
    
    if (request.method=="POST"):
        form = UserProfileForm(data=request.POST, instance=request.user.userprofile, files=request.FILES)
        
        if (form.is_valid()):
            new_form = form.save(commit=False)
            new_form.email = request.user.email
            new_form.save()
            return redirect(to='expense:user_profile')
        else:
            messages.info(request=request, message="Cannot update profile.")

    context = {
        'form': form,
        }
        
    return render(request=request, template_name='expense/profile.html', context=context)


@login_required(login_url='user_login', redirect_field_name=None)
def about(request):
    return render(request=request, template_name='expense/about.html')


@login_required(login_url="user_login", redirect_field_name=None)
def clear_all_expense(request):
    if (request.method == "POST"):
        request.user.userprofile.expense_set.all().delete()
        return redirect(to="expense:index")

    return render(request=request, template_name="expense/confirm_delete.html")


# Graphs for "Analyze More" page
def line_chart(expense_list):

    week_day_list = [0, 0, 0, 0, 0, 0, 0]

    current_date = datetime.datetime.now()                     # returns object
    start_date = datetime.datetime.now() - datetime.timedelta(days=7)           # returns object with hours, min etc.
    start_date = str(start_date.strftime(r"%Y-%m-%d"))         # typecasting in string and converting in required format
    # print(current_date, start_date)
    dataSet = {}            # to store date(key) with all category price(value)

    for expense in expense_list.order_by("-date_added"):
        current_date_str = str(current_date.strftime(r"%Y-%m-%d"))          # string format of date (used for if/else validation)
        current_date_object = datetime.datetime.strptime(current_date_str, r"%Y-%m-%d")           # object of current_date_str (used to get all expense objects of particular date)
        expense_list_current_date = expense_list.filter(date_added__date=current_date_object)
        
        if current_date_str!=start_date:
            category_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 
            for current_date_expense in expense_list_current_date:
                if (current_date_expense.category == 'Food & Drink'):
                    category_list[0] += current_date_expense.price
                elif (current_date_expense.category == 'Shopping'):
                    category_list[1] += current_date_expense.price
                elif (current_date_expense.category == 'Transport'):
                    category_list[2] += current_date_expense.price
                elif (current_date_expense.category == 'Entertainment'):
                    category_list[3] += current_date_expense.price
                elif (current_date_expense.category == 'Healthcare'):
                    category_list[4] += current_date_expense.price
                elif (current_date_expense.category == 'Travel'):
                    category_list[5] += current_date_expense.price
                elif (current_date_expense.category == 'Gifts'):
                    category_list[6] += current_date_expense.price
                elif (current_date_expense.category == 'Education'):
                    category_list[7] += current_date_expense.price
                elif (current_date_expense.category == 'Family & Personal'):
                    category_list[8] += current_date_expense.price
                elif (current_date_expense.category == 'Bills & Fees'):
                    category_list[9] += current_date_expense.price
                elif (current_date_expense.category == 'Groceries'):
                    category_list[10] += current_date_expense.price
                elif (current_date_expense.category == 'Beauty'):
                    category_list[11] += current_date_expense.price
                elif (current_date_expense.category == 'Others'):
                    category_list[12] += current_date_expense.price

            dataSet[current_date_str] = category_list           # {'date1': [categ1, categ2, cate3,.....], 'date2': [...], ...}

            current_date = current_date - datetime.timedelta(days=1)
        else:
            break
            

    
    # logic for chart_obj json format
    dataSource = {}

    dataSource["categories"] = []

    dataSet_keys = list(dataSet.keys())

    for key in dataSet_keys:
        dataSource["categories"].append({'label': key})

# dataSource -> {'categories': [{'label': '2020-12-18'}, {'label': '2020-12-17'}, {'label': '2020-12-16'}, 
#           {'label': '2020-12-15'}, {'label': '2020-12-14'}, {'label': '2020-12-13'}, {'label': '2020-12-12'}]}

    data_list = []
    data_list_data = []
    

    # dataSet (of one 1 day expenses)
    # {'2020-12-29': [0, 0, 0, 0, 0, 0, 0, 0, 23.0, 0, 0, 0, 0]}
    
    if len(dataSet) == 0:       # gives IndexError in next for loop without this logic
        dataSet.setdefault(str(current_date.strftime(r"%Y-%m-%d")), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        dataSet_keys = list(dataSet.keys())

        
    for value in range(len(dataSet[dataSet_keys[0]])):
        for key in dataSet:
            data_list_data.append({'value': dataSet[key][value]})           # price of particular category(key) in different dates(value)
        data_list.append(data_list_data)
        data_list_data = []

# dataSet stores category wise total expense of given date.
# dataSet -> {'2020-12-18': [500.0, 2000.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#   '2020-12-17': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], '2020-12-16': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#   '2020-12-15': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], '2020-12-14': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   '2020-12-13': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], '2020-12-12': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}


    expense_category_name = ['Food & Drink', 'Shopping', 'Transport', 'Entertainment', 'Healthcare', 'Travel', 'Gifts', 'Education', 'Family & Personal', 'Bills & Fees', 'Groceries', 'Beauty', 'Others']

    dataSource["dataset"] = []

    for x in range(13):
        dataSource["dataset"].append({'seriesname': expense_category_name[x], 'data': data_list[x]})        # data structure for required data


#   dataSource (Final)
# dataSource = {'categories': [{'label': '2020-12-18'}, {'label': '2020-12-17'}, {'label': '2020-12-16'}, 
#   {'label': '2020-12-15'}, {'label': '2020-12-14'}, {'label': '2020-12-13'}, {'label': '2020-12-12'}], 
# 
# 'dataset': [{'seriesname': 'Food & Drink', 'data': [{'value': 500.0}, {'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Shopping', 'data': [{'value': 2000.0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0},
#   {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Transport', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Entertainment', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0},
#   {'value': 0}, {'value': 0}]}, {'seriesname': 'Healthcare', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Travel', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Gifts', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}]}, {'seriesname': 'Education', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Family & Personal', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Bills & Fees', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0},
#   {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Groceries', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0},
#   {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Beauty', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}]}, 
#   {'seriesname': 'Others', 'data': [{'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, {'value': 0}, 
#   {'value': 0}, {'value': 0}]}]}


# expense_category_name = ['Food & Drink', 'Shopping', 'Transport', 'Entertainment', 'Healthcare', 'Travel', 
#      'Gifts', 'Education', 'Family & Personal', 'Bills & Fees', 'Groceries', 'Beauty', 'Others']

    today_date = datetime.datetime.now().strftime(r"%Y-%m-%d")
    first_date = (datetime.datetime.now() - datetime.timedelta(days=6)).strftime(r"%Y-%m-%d")
    #### logic completed for json format ###

    try:
        chartObj = FusionCharts( 'msline', 'ex1', '70%', '500', 'chart-1', 'json', {
        "chart": {
            "caption": "Expenses of last 7 days",
            "subcaption": f"{first_date} to {today_date}",
            "yaxisname": "Amount",
            "xaxisname": "Dates",
            "showhovereffect": "1",
            "drawcrossline": "1",
            "plottooltext": "<b>$dataValue</b> were spent on $seriesName",
            "exportEnabled": "1",
            "theme": "candy",
        },
        "categories": [
            {
            "category": [
                {
                "label": dataSource['categories'][6]['label']           # prints dates in x-axis
                },
                {
                "label": dataSource['categories'][5]['label']
                },
                {
                "label": dataSource['categories'][4]['label']
                },
                {
                "label": dataSource['categories'][3]['label']
                },
                {
                "label": dataSource['categories'][2]['label']
                },
                {
                "label": dataSource['categories'][1]['label']
                },
                {
                "label": dataSource['categories'][0]['label']
                }
            ]
            }
        ],
        "dataset": [
            {
            "seriesname": expense_category_name[0],
            "data": [
                {
                "value": dataSource['dataset'][0]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][0]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][0]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][0]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][0]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][0]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][0]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[1],
            "data": [
                {
                "value": dataSource['dataset'][1]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][1]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][1]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][1]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][1]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][1]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][1]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[2],
            "data": [
                {
                "value": dataSource['dataset'][2]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][2]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][2]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][2]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][2]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][2]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][2]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[3],
            "data": [
                {
                "value": dataSource['dataset'][3]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][3]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][3]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][3]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][3]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][3]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][3]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[4],
            "data": [
                {
                "value": dataSource['dataset'][4]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][4]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][4]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][4]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][4]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][4]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][4]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[5],
            "data": [
                {
                "value": dataSource['dataset'][5]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][5]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][5]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][5]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][5]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][5]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][5]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[6],
            "data": [
                {
                "value": dataSource['dataset'][6]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][6]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][6]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][6]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][6]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][6]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][6]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[7],
            "data": [
                {
                "value": dataSource['dataset'][7]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][7]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][7]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][7]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][7]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][7]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][7]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[8],
            "data": [
                {
                "value": dataSource['dataset'][8]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][8]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][8]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][8]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][8]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][8]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][8]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[9],
            "data": [
                {
                "value": dataSource['dataset'][9]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][9]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][9]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][9]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][9]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][9]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][9]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[10],
            "data": [
                {
                "value": dataSource['dataset'][10]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][10]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][10]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][10]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][10]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][10]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][10]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[11],
            "data": [
                {
                "value": dataSource['dataset'][11]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][11]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][11]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][11]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][11]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][11]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][11]['data'][0]['value']
                }
            ]
            },
            {
            "seriesname": expense_category_name[12],
            "data": [
                {
                "value": dataSource['dataset'][12]['data'][6]['value']
                },
                {
                "value": dataSource['dataset'][12]['data'][5]['value']
                },
                {
                "value": dataSource['dataset'][12]['data'][4]['value']
                },
                {
                "value": dataSource['dataset'][12]['data'][3]['value']
                },
                {
                "value": dataSource['dataset'][12]['data'][2]['value']
                },
                {
                "value": dataSource['dataset'][12]['data'][1]['value']
                },
                {
                "value": dataSource['dataset'][12]['data'][0]['value']
                }
            ]
            },        
        ]
        })
    
    except IndexError:
        return None
    except Exception:
        return None

    line_chart_obj = chartObj.render()
    return line_chart_obj
    


def bar_chart(expense_list):

    month_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    current_year = datetime.datetime.now().year

    for expense in expense_list:
        date = getattr(expense, "date_added")           # get expense date (i.e. datetime.datetime(2020, 11, 14, 19, 24, 34, 468013, tzinfo=<UTC>))
        year = date.year                                # get year of expense
        month = date.month                              # get month of expense

        if year == current_year:
            expense_price = getattr(expense, "price")
            if month==1:
                month_list[0] += expense_price
            elif month==2:
                month_list[1] += expense_price
            elif month==3:
                month_list[2] += expense_price
            elif month==4:
                month_list[3] += expense_price
            elif month==5:
                month_list[4] += expense_price
            elif month==6:
                month_list[5] += expense_price
            elif month==7:
                month_list[6] += expense_price
            elif month==8:
                month_list[7] += expense_price
            elif month==9:
                month_list[8] += expense_price
            elif month==10:
                month_list[9] += expense_price
            elif month==11:
                month_list[10] += expense_price
            elif month==12:
                month_list[11] += expense_price
    

    chartObj = FusionCharts( 'column2d', 'ex2', '70%', '500', 'chart-2', 'json', {
    "chart": {
        "caption": "Monthly Expenses",
        "subcaption": f"OF THE YEAR {current_year}",
        "xaxisname": "Months",
        "yaxisname": "Amount",
        "theme": "candy",
        "exportEnabled": "1",
    },
    "data": [
        {
        "label": "Jan",
        "value": month_list[0]
        },
        {
        "label": "Feb",
        "value": month_list[1]
        },
        {
        "label": "Mar",
        "value": month_list[2]
        },
        {
        "label": "Apr",
        "value": month_list[3]
        },
        {
        "label": "May",
        "value": month_list[4]
        },
        {
        "label": "Jun",
        "value": month_list[5]
        },
        {
        "label": "Jul",
        "value": month_list[6]
        },
        {
        "label": "Aug",
        "value": month_list[7]
        },
        {
        "label": "Sep",
        "value": month_list[8]
        },
        {
        "label": "Oct",
        "value": month_list[9]
        },
        {
        "label": "Nov",
        "value": month_list[10]
        },
        {
        "label": "Dec",
        "value": month_list[11]
        }
    ]
    })

    bar_chart_obj = chartObj.render()
    return bar_chart_obj
    # return render(request=request, template_name='expense/graph_analysis.html', context=context)




@login_required(login_url="user_login", redirect_field_name=None)
def graph_analysis(request):

    expense_list = request.user.userprofile.expense_set.all()

    line_chart_obj = line_chart(expense_list)
    bar_chart_obj = bar_chart(expense_list)

    context = {
        'line_chart': line_chart_obj,
        'bar_chart': bar_chart_obj,
        }
    return render(request=request, template_name='expense/graph_analysis.html', context=context)



    # expense_list = request.user.userprofile.expense_set.all().order_by("date_added")


# Note use getattr()
# >>> value = getattr(Expense.objects.last(), "date_added")
# >>> value
# datetime.datetime(2020, 11, 14, 19, 24, 34, 468013, tzinfo=<UTC>)
