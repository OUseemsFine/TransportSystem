from django.db import models

# Create your models here.
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

class Busline(models.Model):
    """Model to represent a busline"""
    LINE_STATUS= (
        ('m', '维护中'),
        ('o', '运营中'),
        ('b', '建设中'),
    )
    status = models.CharField(max_length=1, choices=LINE_STATUS ,default='b')
    startTime = models.TimeField(help_text="Start time")
    endTime = models.TimeField(help_text="End time")
    lineNumber = models.PositiveIntegerField(unique=True, help_text="set a unique line number")
    Price = models.DecimalField(max_digits=10, decimal_places=2, help_text="set a price")
    description = models.TextField(help_text="describe this bus line")
    
    def __str__(self):
        """String for representing the Model object."""
        return f'No.{self.lineNumber} bus line'

class StationSequence(models.Model):
    """Model to represent a staion's information(belong to which line, sequence in a line)"""
    station = models.ForeignKey('Station', on_delete=models.CASCADE, help_text="select a staion")
    busline = models.ForeignKey('Busline', on_delete=models.CASCADE, help_text="select a busline", null=True)
    order = models.PositiveIntegerField()
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} (staion_sequence)'
    

class Station(models.Model):
    """model of staions"""
    sName = models.CharField(
        max_length=200,
        help_text="Enter a staion name",
        unique=True
    )
    
    STATION_STATUS =  (
        ('m', '维护中'),
        ('o', '运营中'),
        ('b', '建设中'),
    )
    status = models.CharField(max_length=1, choices=STATION_STATUS, default='b')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.sName
    

class Position(models.Model):
    """Model representing a position genre."""
    pName = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a position (e.g. Driver ...)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.pName

    def get_absolute_url(self):
        """Returns the url to access a particular position ."""
        return reverse('position-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('pName'),
                name='position_pname_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]

class Department(models.Model):
    """Model representing a department."""
    dName = models.CharField(max_length=200)
    dSummary = models.TextField(
        max_length=1000, help_text="Enter a description of the department"
    )
    positions = models.ManyToManyField(Position, help_text="Select a position for this department", blank=True) 
    
    class Meta:
        ordering = ['dName']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.dName

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this department."""
        return reverse('department-detail', args=[str(self.id)])

import uuid # Required for unique Employee 

class Employee(models.Model):

    """Model representing an Employee."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular Employee")
    eName = models.CharField(max_length=200)
    birthDate = models.DateField(help_text="Enter the employee's birth date")
    eResume = models.TextField(max_length=1000, help_text="Enter the description of this staff")
    hireDate = models.DateField(help_text="Enter the employee's hired date")
    eSalary = models.DecimalField(
        max_digits=10,  
        decimal_places=2, 
        help_text="Enter the employee's monthly salary"
    )
    
    department = models.ForeignKey(Department, on_delete=models.RESTRICT, null=True,help_text="Select a department for this employee")
    position = models.ForeignKey(Position, on_delete=models.RESTRICT, null=True, help_text="Select a position for this employee")

    class Meta:
        ordering = ['eName']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.eName} - {self.position})'
    
    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])


class Vehicle(models.Model):
    '''Model representing a vehicle type'''
    vModel = models.CharField(max_length=200, unique=True)
    BUS_TYPE= (
        ('n', '普通公交车'),
        ('m', '微型公交车'),
        ('j', '大型公交车'),
        ('c','柴油公交车'),
        ('d','电动公交车'),
    )
    vType = models.CharField(max_length=1, choices=BUS_TYPE ,default='n')
    manufacturer = models.CharField(max_length=200)
    capacity = models.IntegerField(help_text="Please input the capacity of this vehicle")
    description = models.TextField();
    
        
    def __str__(self):
        """String for representing the Model object."""
        return self.vModel
    
    
    
import random
import string
def generate_random_plate_number():
        """Generate a random license plate number."""
        # province_code = random.choice(['京', '津', '沪', '粤', '川', '浙', '苏', '晋', '闽', '蒙', 
        #                                 '桂', '陕', '吉', '黑', '辽', '鄂', '湘', '皖', '鲁', 
        #                                 '贵', '青', '新', '藏', '琼', '宁', '港', '澳'])
        province_code = '渝'
        letter = random.choice(string.ascii_uppercase)  # 随机字母
        digits = ''.join(random.choices(string.digits, k=5))  # 随机5位数字
        return f"{province_code}{letter}{digits}"


class VehicleInstance(models.Model):
    '''Model representing a vehivle instance'''
    
    vehicle = models.ForeignKey('Vehicle', on_delete=models.RESTRICT, help_text="Choose a vehicle")
    plateNumber = models.CharField(max_length=200, primary_key=True, default=generate_random_plate_number()) 
    last_maintenance_date = models.DateField(blank=True);
    produce_date = models.DateField(help_text="Input the produced date");
    
    
    busline = models.ForeignKey('Busline',on_delete=models.SET_NULL,null = True,help_text="choose a bus-line")
    
    BUS_STATUS= (
        ('m', '维护中'),
        ('o', '运营中'),
    )
    status = models.CharField(max_length=1, choices=BUS_STATUS ,default='o')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.plateNumber
    


    # def save(self, *args, **kwargs):
    #     """Override the save method to set a random plate number as the default."""
    #     if not self.plateNumber:
    #         self.plateNumber = generate_random_plate_number()
    #     super().save(*args, **kwargs)
    
    
    
    