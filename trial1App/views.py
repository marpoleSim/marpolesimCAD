from django.shortcuts import render
from django.http import JsonResponse
from .cadquery import simpleBlock
from django.conf import settings as django_settings

# Create your views here.
def trial(request):

    return render(request, 'index.html')

def setHole(request):

    if request.method == 'POST':

       x = request.POST.get('x')
       y = request.POST.get('y')
       diameter = request.POST.get('d')
       
       vtpROOTPath = str(django_settings.MEDIA_ROOT) + '/trial1'
       vtpURLPath = str(django_settings.MEDIA_URL) + 'trial1'
       filename = simpleBlock.simpleBlock(x, y, diameter, vtpROOTPath)
       data = {'vtpURLPath': vtpURLPath}
       return JsonResponse(data)

