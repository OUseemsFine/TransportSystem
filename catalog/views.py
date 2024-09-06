from django.shortcuts import render

# Create your views here.
from .models import Position, Employee, Department

def index(request):
    """View function for home page of site."""

    context = {
        'num_books': 0,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class DepartmentListView(generic.ListView):
    model = Department
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for department in context['department_list']:
            department.position_count = department.positions.count()
        return context
    
class DepartmentDetailView(generic.DetailView):
    model = Department
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(department=self.object)
        return context
    
    
class EmployeeDetailView(generic.DetailView):
    model = Employee

# views.py
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Department

def add_employee(request):
    departments = Department.objects.all()  # 获取所有部门
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 重定向到员工列表页面
    else:
        form = EmployeeForm()

    return render(request, 'catalog/add_employee.html', {'form': form, 'department_list': departments})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmployeeUpdateForm
from .models import Employee, Department

def update_employee(request, pk):
    # 使用 pk 获取员工对象
    employee = get_object_or_404(Employee, id=pk)
    departments = Department.objects.all()  # 获取所有部门

    if request.method == "POST":
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-detail', pk=employee.id)  # 使用 pk 重定向到员工详情页面
        else:
            print(form.errors)  # 打印错误信息以调试
    else:
        form = EmployeeUpdateForm(instance=employee)

    return render(request, 'catalog/update_employee.html', {
        'form': form,
        'employee': employee,
        'departments': departments
    })
    
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    '''This is the api to get a scrf token'''
    return JsonResponse({'csrfToken': get_token(request)})  

from rest_framework import generics
from .models import Station
from .serializers import StationCreateSerializer

class StationCreateView(generics.CreateAPIView):
    '''This is the api to add new station'''
    queryset = Station.objects.all()
    serializer_class = StationCreateSerializer

    def perform_create(self, serializer):
        # 在保存之前设置默认状态
        serializer.save(status='b')
        
        
from rest_framework import generics
from .models import Station
from .serializers import StationGetSerializer

class StationListView(generics.ListAPIView):
    '''This is the api to fetch all the stations'''
    queryset = Station.objects.all()
    serializer_class = StationGetSerializer
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Station

@api_view(['GET'])
def check_station_name(request):
    '''this is the api to check if the station name has already existed'''
    sName = request.GET.get('sName', None)
    if sName is not None:
        exists = Station.objects.filter(sName=sName).exists()
        return Response({'exists': exists})
    return Response({'exists': False}, status=400)

from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Station
from .serializers import StationSerializer

class StationUpdateView(generics.UpdateAPIView):
    '''This is the api to update station's status, location info'''
    serializer_class = StationSerializer

    def get_object(self):
        # 从请求数据中获取 sName
        s_name = self.request.data.get('sName')
        # 根据 sName 查找 Station 对象
        return get_object_or_404(Station, sName=s_name)

    def patch(self, request, *args, **kwargs):
        station = self.get_object()
        
        if 'status' in request.data:
            status_value = request.data['status']

        # 更新 Station 对象
        serializer = self.get_serializer(station, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# views.py
from rest_framework import generics
from .models import Busline
from .serializers import BuslineSerializer

class BuslineCreateView(generics.CreateAPIView):
    '''This is the api to add a busline'''
    queryset = Busline.objects.all()
    serializer_class = BuslineSerializer
    
# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Busline

class BuslineExistsView(generics.GenericAPIView):
    '''This is the api to check if a bus-line number has been used'''
    def get(self, request, line_number):
        try:
            busline = Busline.objects.get(lineNumber=line_number)
            return Response({'exists': True}, status=status.HTTP_200_OK)
        except Busline.DoesNotExist:
            return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND)