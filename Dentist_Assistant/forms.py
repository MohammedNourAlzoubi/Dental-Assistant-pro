from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
 
 class Meta:
        model=Patient
        fields = ['name','age','phone','progress','gender','work','marital_status'] 
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'progress': forms.Select(attrs={'class':'form-select'}),
            'gender': forms.Select(attrs={'class':'form-select'}),
            'work': forms.TextInput(attrs={'class':'form-control'}),
            'marital_status': forms.Select(attrs={'class':'form-select'}),
        }


