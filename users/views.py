from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import  RegisterForm
from django.contrib.auth import login,logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            welcome_message =f'Welcome {user}, your account is created successfully'
            user.save()
            messages.success(request,welcome_message)
            # login(request,user)
            return redirect('login')

    else:
        form = RegisterForm()


    return render(request,'users/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    return render(request,'users/logout.html')
    # return redirect('login')

