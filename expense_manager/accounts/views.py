from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from .decorators import is_authenticated
from django.views.decorators.debug import sensitive_variables


# User Register, Login, Logout
@is_authenticated
def userRegister(request):
    form = UserRegisterForm()
    
    if (request.method=="POST"):
        form = UserRegisterForm(request.POST)

        if (form.is_valid()):
            user = form.save()
            return redirect(to='expense:index')
        else:
            messages.info(request=request, message="User already exists or Password do not match.")
        
    context = {'form': form}
    return render(request=request, template_name='accounts/register.html', context=context)

@is_authenticated
@sensitive_variables('username', 'password')
def userLogin(request):
    if (request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        
        if (user is not None):
            login(request=request, user=user)
            return redirect(to='expense:index')
        else:
            messages.info(request=request, message="Invalid user or Wrong password")

    return render(request=request, template_name='accounts/login.html')

def userLogout(request):
    logout(request=request)
    return redirect(to='expense:index')




