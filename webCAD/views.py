from django.shortcuts import render, redirect
from accounts.models import UserType

from django.contrib.sessions.models import Session 
from django.utils.timezone import now

# Create your views here.
def home(request):

    if request.user.is_authenticated:
        user = request.user 

        # check if it is admin
        if user.username == 'marpolesim': 
            # Find all active sessions
            sessions = Session.objects.filter(expire_date__gte=now())
        
            for session in sessions:
                data = session.get_decoded()
                if data.get('_auth_user_id') == str(user.id):  # Match user ID in session 
                    session.delete()  # Delete session to log the user out
            return render(request, 'coverPage.html')
        else:
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
