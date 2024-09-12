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
    
from rest_framework import generics
from .models import Busline
from .serializers import BuslineSerializer

class BuslineListView(generics.ListAPIView):
    '''This is the api to fetch all the bus-lines'''
    queryset = Busline.objects.all()
    serializer_class = BuslineSerializer
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Station
    

from rest_framework import generics
from .models import Busline
from .serializers import BuslineSerializer

class BuslineCreateView(generics.CreateAPIView):
    '''This is the api to add a busline'''
    queryset = Busline.objects.all()
    serializer_class = BuslineSerializer
    

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
            return Response({'exists': False}, status=status.HTTP_200_OK)
        
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Busline
from .serializers import BuslineSerializer    

class BuslineDetailView(generics.RetrieveAPIView):
    '''This is the API to get bus-line info via input lineNumber'''        
    queryset = Busline.objects.all()
    serializer_class = BuslineSerializer
    
    def get(self, request, line_number):
        try:
            busline = Busline.objects.get(lineNumber=line_number)
            serializer = self.get_serializer(busline)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Busline.DoesNotExist:
            return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND)
        
from rest_framework import generics
from .models import StationSequence
from .serializers import StationSequenceSerializer
from rest_framework.response import Response
from rest_framework import status

class StationSequenceCreate(generics.CreateAPIView):
    '''This is the API to create a station sequence'''
    queryset = StationSequence.objects.all()
    serializer_class = StationSequenceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            station_sequence = serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StationSequence
from .serializers import StationSequenceSerializer

class StationSequenceList(APIView):
    '''This is the API to fetch station sequences by busline number'''
    def get(self, request, line_number):
        station_sequences = StationSequence.objects.filter(busline__lineNumber=line_number)
        if station_sequences.exists():
            serializer = StationSequenceSerializer(station_sequences, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND)
            
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Busline
from .serializers import BuslineSerializer

class BuslineUpdateView(generics.UpdateAPIView):
    '''This is the api to update bus-line'''
    serializer_class = BuslineSerializer

    def get_object(self):
        lineNumber = self.request.data.get('lineNumber')
        return get_object_or_404(Busline, lineNumber=lineNumber)

    def patch(self, request, *args, **kwargs):
        busline = self.get_object()
        
        if 'status' in request.data:
            status_value = request.data['status']

        # 更新 Busline 对象
        serializer = self.get_serializer(busline, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StationSequence
from .serializers import StationDataSerializer


@api_view(['POST'])
def update_station_sequences(request, busline_id):
    """
    更新与给定 busline_id 相关的 StationSequence 实例。
    :param busline_id: 公交线路的 ID
    :param request: 包含 station_data 的请求数据
    :examle:
const buslineId = 1; // 替换为实际的 busline ID
const stationData = [
    { station_id: 1, order: 1 },
    { station_id: 2, order: 2 },
    { station_id: 3, order: 3 }
];

async function updateStationSequences(buslineId, stationData) {
    try {
        const response = await fetch(`/busline/${buslineId}/stations/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ stations: stationData }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Error updating station sequences:', errorData);
        } else {
            const result = await response.json();
            console.log('Station sequences updated successfully:', result);
        }
    } catch (error) {
        console.error('Network error:', error);
    }
}
    """
    station_data = request.data.get('stations', [])
    
    # 删除集合 A 中存在但集合 B 中没有的 station_id
    current_sequences = StationSequence.objects.filter(busline_id=busline_id)
    current_station_ids = {seq.station_id for seq in current_sequences}

    new_station_ids = {data['station_id'] for data in station_data}

    # 删除不在新数据中的站点
    for sequence in current_sequences:
        if sequence.station_id not in new_station_ids:
            sequence.delete()

    # 添加或更新新的 StationSequence 实例
    for data in station_data:
        StationSequence.objects.update_or_create(
            busline_id=busline_id,
            station_id=data['station_id'],
            defaults={'order': data['order']}
        )

    return Response({'status': station_data}, status=status.HTTP_200_OK)

# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Busline
from .serializers import BuslineSerializer

class BuslineDeleteView(APIView):
    '''This is the API to delete a bus-line'''
    def delete(self, request, line_number):
        try:
            busline = Busline.objects.get(lineNumber=line_number)
            busline.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Busline.DoesNotExist:
            return Response({"error": "Busline not found."}, status=status.HTTP_404_NOT_FOUND)
        
from rest_framework import generics
from .models import VehicleInstance
from .serializers import VehicleInstanceSerializer

class VehicleInstanceListView(generics.ListAPIView):
    '''This is the api to fetch all the vehicle instances'''
    queryset = VehicleInstance.objects.all()
    serializer_class = VehicleInstanceSerializer