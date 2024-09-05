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
    station = models.ForeignKey('Station', on_delete=models.RESTRICT, help_text="select a staion")
    busline = models.ForeignKey('Busline', on_delete=models.RESTRICT, help_text="select a busline", null=True)
    order = models.PositiveIntegerField()
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} (staion_sequence)'
    

class Station(models.Model):
    """model of staions"""
    sName = models.CharField(
        max_length=200,
        help_text="Enter a staion name"
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
