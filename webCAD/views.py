from django.shortcuts import render, redirect
from accounts.models import UserType

# Create your views here.
def home(request):

    if request.user.is_authenticated:
      userType = UserType.objects.get(user = request.user)
      if userType.isCompany:
        return redirect('company_cover_page')
      else:
        return redirect('user_cover_page')
    else:
        return render(request, 'coverPage.html')

def user_cover_page(request):

    return render(request, 'user_cover_page.html')

def company_cover_page(request):

    return render(request, 'company_cover_page.html')

def about(request):

    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')
