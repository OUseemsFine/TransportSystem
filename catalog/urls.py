from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('department/<int:pk>',views.DepartmentDetailView.as_view(), name='department-detail'),
    path('department/employee/<uuid:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
]

