from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
]

