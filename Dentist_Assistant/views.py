from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient
from django.contrib import messages



# Create your views here.
def overview(request):
    patients=Patient.objects.all().order_by("-id")
    context = {"patients":patients}
    return render(request,"overview.html",context)
# #################################################
# def patient_profile(request):
#     return render(request,"patient_profile_1.html")
# #################################################
def patient_profile(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            newform = form.save(commit = False)       
            newform.save()
            return redirect('patient_profile')
    form = PatientForm()
    context = {"form":form}
    return render(request,"patient_profile_1.html",context)


# #############################################################
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if(patient.delete()):
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('index')
    context = {'patient': patient}
    return render(request, 'overview.html',context )
