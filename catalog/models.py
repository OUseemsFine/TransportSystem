from django.db import models

# Create your models here.
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

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
