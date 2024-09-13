from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('department/<int:pk>',views.DepartmentDetailView.as_view(), name='department-detail'),
    path('department/employee/<uuid:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
]

# urls.py
from .views import add_employee

urlpatterns += [
    path('department/employee/add', add_employee, name='add-employee'),  # 添加员工的 URL
    path('department/employee/update/<uuid:pk>', views.update_employee, name='employee-update'),  # 修改员工的 URL
]

################# API part start
from .views import get_csrf_token  
urlpatterns += [
    path('api/get-csrf-token/', get_csrf_token, name='get-csrf-token'), # get csrf token
]

##### API of station
##station:
from .views import StationCreateView, StationListView, check_station_name, StationUpdateView
urlpatterns += [
    path('api/stations/add', StationCreateView.as_view(), name='station-add'),
    path('api/stations/list', StationListView.as_view(), name='station-list'),
    path('api/stations/check-name', check_station_name, name='check_station_name'),
    path('api/stations/update', StationUpdateView.as_view(), name='station-update'),
]

##busline:
from .views import BuslineCreateView,BuslineExistsView,BuslineDetailView,BuslineListView,BuslineUpdateView,BuslineDeleteView
urlpatterns += [
    path('api/busline/add', BuslineCreateView.as_view(), name='busline-create'),
    path('api/busline/exist/<int:line_number>',BuslineExistsView.as_view(),name='busline-ifexist'),
    path('api/busline/get/<int:line_number>',BuslineDetailView.as_view(),name='busline-get'),
    path('api/busline/get/all',BuslineListView.as_view(),name='busline-getAll'),
    path('api/busline/update',BuslineUpdateView.as_view(),name='busline-update'),
    path('api/busline/delete/<int:line_number>',BuslineDeleteView.as_view(),name='busline-delete'),
]

from .views import StationSequenceCreate,StationSequenceList,update_station_sequences
##StationSequence:
urlpatterns += [
    path('api/stationSequence/add',StationSequenceCreate.as_view(),name="station_sequence-add"),
    path('api/stationSequence/fetch/lineNumber/<int:line_number>',StationSequenceList.as_view(),name="station_sequence-getByline"),
    path('api/stationSequence/update/<int:busline_id>', update_station_sequences, name='update_station_sequences'),
]

from .views import VehicleInstanceListView, VehicleInstanceCreateAPIView, VehicleListView, VehicleInstanceUpdateAPIView
urlpatterns += [
    path('api/vehicle/model/all',VehicleListView.as_view(),name="vehicleModel-get"),
    path('api/vehicle/fetch/all',VehicleInstanceListView.as_view(),name="vehicle-get"),
    path('api/vehicle/add',VehicleInstanceCreateAPIView.as_view(),name="vehicle-add"),
    path('api/vehicle/update/<str:plateNumber>',VehicleInstanceUpdateAPIView.as_view(),name="vehicle-update"),
]


################### API part end

