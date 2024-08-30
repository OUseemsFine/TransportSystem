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
 
    