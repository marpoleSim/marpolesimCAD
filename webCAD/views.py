from django.shortcuts import render, redirect
from accounts.models import UserType

# Create your views here.
def home(request):

    if request.user.is_authenticated:
      userType = UserType.objects.get(user = request.user)
      if userType.isCompany:
        return redirect('reviewOrder')
      else:
        return redirect('selectPart')
    else:
        return render(request, 'coverPage.html')

