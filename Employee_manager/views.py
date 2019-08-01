from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from Employee_manager.serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Employee_manager.models import Employee
from Employee_manager.models import Group
from Employee_manager.models import Manager
from Employee_manager.serializers import EmployeeSerializer


@csrf_exempt
def company_view(request, group_id):
    if request.method == 'GET':
        employees = Employee.objects.filter(group=group_id)
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def add_employee_view(request):

    if request.method == 'GET':
        employees = Employee.objects.filter(id=1)
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT'])
@csrf_exempt
def change_employee_view(request, employee_id, group_id):
    if request.method == 'GET':
        employees = Employee.objects.filter(id=1)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        # data = JSONParser().parse(request)
        e = Employee.objects.get(id=employee_id)
        e.group = Group.objects.get(id=group_id)
        e.manager = e.group.manager
        e.save()
        serializer = EmployeeSerializer(e)
        return JsonResponse(serializer.data, status=201)



@csrf_exempt
def delete_employee_view(request, employee_id):
    if request.method == 'PUT':
        e = Employee.objects.get(id=employee_id)
        e.group = None
        e.manager = None
        e.save()
        serializer = EmployeeSerializer(e)
        return JsonResponse(serializer.data)

@csrf_exempt
def display_something(request):
    return HttpResponse('Hello World!')
