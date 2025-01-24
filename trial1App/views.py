from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings as django_settings
from django.http import FileResponse

import trial1App.backend.buildPart as bp 

from .models import Part, Order

# Create your views here.
def trial(request):

    partName = Part.objects.filter().values_list('partName', flat=True)

    partNameList = list(partName)

    data = {'inputList': partNameList}

    return render(request, 'index.html', data)

def geomParameter(request):

    partName = request.POST.get('selectPart')
    part = Part.objects.filter(partName = partName).values() 
    partDict = list(part)[0] 
    numberOfArgs = partDict['numberOfArgs']
    functionName = partDict['functionName']
  
    argName=[None]*numberOfArgs 
    argValue=[None]*numberOfArgs 

    for i in range(numberOfArgs):
       argName[i] = partDict['arg' + str(i) + 'Name']
       argValue[i] = partDict['arg' + str(i) + 'Value']

    return JsonResponse({'partName': partName, 'functionName': functionName, 'numberOfArgs': numberOfArgs, 'argNames': argName, 'argValues': argValue})

def modelling(request):

    if request.method == 'POST':
       partName = request.POST.get('selectPart')
       part = Part.objects.filter(partName = partName).values() 
       functionName = list(part)[0]['functionName']
       vtpRootPath = str(django_settings.MEDIA_ROOT) + '/trial1'

       arg = [0]*9
       for i in range(9):
         arg[i] = float(request.POST.get('argvalue'+str(i+1)))
       
       flag = bp.buildPart(partName, functionName, arg, vtpRootPath)
       data = {'flag': flag, 'partName': partName,}
       return JsonResponse(data)

def savePart(request):

    if request.method == 'POST':
       partName = request.POST.get('selectPart')

       newPartName = request.POST.get('newPartName')

       flag = True 
       if not Order.objects.filter(partName = newPartName).exists():

           part = Part.objects.filter(partName = partName).values()
           partDict = list(part)[0]
           numberOfArgs = partDict['numberOfArgs']

           arg = [0]*9
           for i in range(9):
             arg[i] = float(request.POST.get('argvalue'+str(i+1)))
    
           newOrder = Order(partName = newPartName, templateName = partName, userName = 'dummy', numberOfArgs = numberOfArgs, 
                            arg0Name = partDict['arg0Name'], arg0Value= arg[0], 
                            arg1Name = partDict['arg1Name'], arg1Value= arg[1], 
                            arg2Name = partDict['arg2Name'], arg2Value= arg[2], 
                            arg3Name = partDict['arg3Name'], arg3Value= arg[3], 
                            arg4Name = partDict['arg4Name'], arg4Value= arg[4], 
                            arg5Name = partDict['arg5Name'], arg5Value= arg[5], 
                            arg6Name = partDict['arg6Name'], arg6Value= arg[6], 
                            arg7Name = partDict['arg7Name'], arg7Value= arg[7], 
                            arg8Name = partDict['arg8Name'], arg8Value= arg[8], )
           newOrder.save() 
       else:
           flag = False

       data = {'flag': flag}
       return JsonResponse(data)
