from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

#from .models import UserType, CustomerInfo
#from .forms import SignUpForm, ContactForm, UserTypeForm, CustomerInfoForm

from .models import UserType
from .forms import SignUpForm, UserTypeForm, CompanyInfoForm

def user_login_view(request):

    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])

        # check if the user is company        
        flag = True
        if UserType.objects.filter(user = user).exists(): 
           user_type = UserType.objects.get(user = user) 
           flag = not user_type.isCompany
        else:
           flag = False 
        
        if user and flag:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'user_login.html', {"error": "login error"})

    return render(request, 'user_login.html')

def user_signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        userTypeForm = UserTypeForm(request.POST) 
        if form.is_valid() and userTypeForm.is_valid():
            user=form.save()
            userTypeForm.save(commit=False)
            userTypeForm.instance.isCompany = False
            userTypeForm.instance.user = user
            userTypeForm.save()
            return redirect('user_login')
        else:
            return render(request, 'user_signup.html', {'form': form, 'error': 'signup error, username is already used, or password is too weak'})
    else:
        form = SignUpForm()

    return render(request, 'user_signup.html', {'form': form})

def company_login_view(request):

    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])

        # check if the user is company        
        flag = True
        if UserType.objects.filter(user = user).exists(): 
           user_type = UserType.objects.get(user = user)
           flag = user_type.isCompany
        else:
           flag = False
        
        if user and flag:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'company_login.html', {"error": "login error, or user is not a company."})

    return render(request, 'company_login.html')

def company_signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        userTypeForm = UserTypeForm(request.POST) 
        companyInfoForm = CompanyInfoForm(request.POST) 
        if form.is_valid() and userTypeForm.is_valid() and companyInfoForm.is_valid():
            user=form.save()
   
            # user type
            userTypeForm.save(commit=False)
            userTypeForm.instance.isCompany = True 
            userTypeForm.instance.user = user
            userTypeForm.save()

            # company info
            companyInfoForm.save(commit=False)
            companyInfoForm.instance.user = user
            companyInfoForm.save()
            return redirect('company_login')
        else:
            return render(request, 'company_signup.html', {'form': form, 'companyInfoForm': companyInfoForm, 'error': 'signup error, username is already used, or password is too weak'})
    else:
        form = SignUpForm()
        companyInfoForm = CompanyInfoForm()

    return render(request, 'company_signup.html', {'form': form, 'companyInfoForm': companyInfoForm, })

def customer_info_view(request):

    # if it is filled up
    if request.method == "POST":
        form = CustomerInfoForm(request.POST) 
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home') 
    else:
    # if it is not filled up
        form = CustomerInfoForm() 

    # if it is not filled up or if the form is invalid
    return render(request, 'customerInfo.html', {'form': form})

