from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings as django_settings
from django.http import FileResponse
from django.forms.models import model_to_dict

import trial1App.backend.buildPart as bp 

from .models import Part, Order
from accounts.models import CompanyInfo

# Create your views here.
def trial(request):
    if request.method == 'POST':
       partName = request.POST.get('partList')
       part = Part.objects.filter(partName = partName).values()[0] 
       numberOfArgs = part['numberOfArgs']
       argName=['dummy']*9
       argValue=[0]*9
       argState=['none']*9 

       for i in range(numberOfArgs):
          argName[i] = part['arg' + str(i) + 'Name'] 
          argValue[i] = part['arg' + str(i) + 'Value']
          argState[i] = 'block' 

       argList = list(zip(argName, argValue, argState))

       data = {'partname': partName, 'numberOfArgs': numberOfArgs, 'argList': argList}

    return render(request, 'trial.html', data)

def geomParameter(request):

    partName = request.POST.get('selectPart')
    part = Part.objects.filter(partName = partName).values() 
    partDict = list(part)[0] 
    numberOfArgs = partDict['numberOfArgs']
    #functionName = partDict['functionName']
    functionName = partName
  
    argName=[None]*numberOfArgs 
    argValue=[None]*numberOfArgs 

    for i in range(numberOfArgs):
       argName[i] = partDict['arg' + str(i) + 'Name']
       argValue[i] = partDict['arg' + str(i) + 'Value']

    return JsonResponse({'partName': partName, 'functionName': functionName, 'numberOfArgs': numberOfArgs, 'argNames': argName, 'argValues': argValue})

def modelling(request):

    if request.method == 'POST':
       partName = request.POST.get('partname')
       #part = Part.objects.filter(partName = partName).values() 
       #functionName = list(part)[0]['functionName']
       functionName = partName
       vtpRootPath = str(django_settings.MEDIA_ROOT) + '/trial1'

       args = request.POST.getlist('argvalue')

       for i in range(len(args)):
         args[i] = float(args[i])

       flag = bp.buildPart(partName, functionName, args, vtpRootPath)
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

def select_company(request):

    objs = CompanyInfo.objects.all() 
    objList = list(objs.values())
    companyList = [ x['company'] for x in objList]

    return render(request, 'selectCompany.html', {'companyList': companyList, })

def select_companyB(request):

    if request.method == 'POST':
       companyName = request.POST.get('companyList')

       # search parts
       company = CompanyInfo.objects.filter(company = companyName)[0]
       partObjs = Part.objects.filter(company = company)
       parts = partObjs.values_list('partName', flat=True).distinct()
       partList = list(parts)

       data = {'partList': partList,}
       return JsonResponse(data)

def select_part(request):

    if request.method == 'POST':
       companyName = request.POST.get('companyList')
       company = CompanyInfo.objects.filter(company = companyName)[0]
       partObjs = Part.objects.filter(company = company)
       parts = partObjs.values_list('partName', flat=True).distinct()
       partList = list(parts)

    return render(request, 'selectPart.html', {'partList': partList, })


def submit_order(request):

    if request.method == 'POST':
       part_name = request.POST.get('partnameB')
       part = Part.objects.filter(partName = part_name)[0]
       company = part.company 
       company_name = company.company
       user = request.user 
       argvalueB1 = request.POST.get('argvalueB1')
       argvalueB2 = request.POST.get('argvalueB2')
       argvalueB3 = request.POST.get('argvalueB3')
       argvalueB4 = request.POST.get('argvalueB4')
       argvalueB5 = request.POST.get('argvalueB5')
       argvalueB6 = request.POST.get('argvalueB6')
       argvalueB7 = request.POST.get('argvalueB7')
       argvalueB8 = request.POST.get('argvalueB8')
       argvalueB9 = request.POST.get('argvalueB9')
       new_order = Order()
       new_order.user = user
       new_order.company = company
       new_order.part = part
       new_order.arg0Value = float(argvalueB1)   
       new_order.arg1Value = float(argvalueB2)   
       new_order.arg2Value = float(argvalueB3)   
       new_order.arg3Value = float(argvalueB4)   
       new_order.arg4Value = float(argvalueB5)   
       new_order.arg5Value = float(argvalueB6)   
       new_order.arg6Value = float(argvalueB7)   
       new_order.arg7Value = float(argvalueB8)   
       new_order.arg8Value = float(argvalueB9)
       new_order.save()
       order_id = 10000 + new_order.id
       order_time = str(new_order.orderDate)
       data = [ order_id, order_time, part_name, company_name, user.username ] 

       numberOfArgs = part.numberOfArgs 
       arg_names=[None]*numberOfArgs
       arg_values=[None]*numberOfArgs

       partDict = model_to_dict(part)
       newPartDict = model_to_dict(new_order)

       for i in range(numberOfArgs):
          arg_names[i] = partDict['arg' + str(i) + 'Name']
          arg_values[i] = newPartDict['arg' + str(i) + 'Value']

       argList = list(zip(arg_names, arg_values,))   
    
       data = {}
       data['order_id'] = order_id
       data['order_time'] = order_time
       data['part_name'] = part_name
       data['company_name'] = company_name
       data['user_name'] = user.username
       data['parameterList'] = argList

    return render(request, 'order_receipt.html', data)

def user_review_order(request):

    #get user
    user = request.user

    #search order table
    orders = Order.objects.filter(user = user)
    
    #get a list
    #find part, date, 
    orderIDList = []
    orderPartNameList = []
    orderCompanyList = []
    orderDateList = []

    for order in orders: 
        orderIDList.append( order.id+10000 )
        orderPartNameList.append(order.part.partName)
        orderCompanyList.append(order.company.company)
        orderDateList.append(order.orderDate.strftime('%Y-%m-%d %H:%M'))

    orderList = list(zip(orderIDList, orderPartNameList, orderCompanyList, orderDateList,))    
 
    return render(request, 'user_review_order.html', {'orderList': orderList} )
