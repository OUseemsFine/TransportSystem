# forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'eName',
            'birthDate',
            'eResume',
            'hireDate',
            'eSalary',
            'department',  # 包含部门字段
             'position' ,
        ]
        widgets = {
            'birthDate': forms.DateInput(attrs={'type': 'date'}),
            'hireDate': forms.DateInput(attrs={'type': 'date'}),
            'eResume': forms.Textarea(attrs={'rows': 4}),
        }
        

from django import forms
from .models import Employee

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'eName',      # 姓名
            'birthDate',  # 生日
            'eResume',    # 简历
            'eSalary',    # 工资
            'department',  # 部门
            'position',    # 职位
        ]
        widgets = {
            'birthDate': forms.DateInput(attrs={'type': 'date'}),
            'eResume': forms.Textarea(attrs={'rows': 4}),
            'eName': forms.TextInput(attrs={'readonly': 'readonly'}),  # 姓名只读
        }