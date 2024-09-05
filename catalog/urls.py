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

# add API urls here: 
from .views import get_csrf_token  

urlpatterns += [
    path('api/get-csrf-token/', get_csrf_token, name='get-csrf-token'), # get csrf token
]


from django.urls import path
from .views import StationCreateView
urlpatterns += [
    path('api/stations/add', StationCreateView.as_view(), name='station-add'),
]