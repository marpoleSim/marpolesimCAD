from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings as django_settings

import trial1App.backend.buildPart as bp 

# Create your views here.
def trial(request):

    return render(request, 'index.html')

def modelling(request):

    arg = [0]*9

    if request.method == 'POST':

       arg[0] = float(request.POST.get('arg0'))
       arg[1] = float(request.POST.get('arg1'))
       arg[2] = float(request.POST.get('arg2'))
       arg[3] = float(request.POST.get('arg3'))
       arg[4] = float(request.POST.get('arg4'))
       arg[5] = float(request.POST.get('arg5'))
       arg[6] = float(request.POST.get('arg6'))
       arg[7] = float(request.POST.get('arg7'))
       arg[8] = float(request.POST.get('arg8'))
       
       vtpRootPath = str(django_settings.MEDIA_ROOT) + '/trial1'
       filename = bp.buildPart('myPart','rectanglePlate', arg, vtpRootPath)
       data = {'filename': filename}
       return JsonResponse(data)

