from django.db import models

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]
MARITAL_CHOICES = [
    ('S', 'Single'),
    ('M', 'Married')
]
PROGRESS_CHOICES = [
    ('B', 'Beginning'),
    ('I', 'In Progress'),
    ('C', 'Completed')
]
class Patient(models.Model):
    
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    progress = models.CharField(max_length=1, choices=PROGRESS_CHOICES, blank=True, null=True,default='B')
    start_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True,default='M')
    work = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_CHOICES, blank=True, null=True,default='S')

    def __str__(self):
        return self.name
