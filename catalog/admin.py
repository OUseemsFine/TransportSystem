from django.contrib import admin

# Register your models here.
from .models import Position, Employee, Department

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Department)
