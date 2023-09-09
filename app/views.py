from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def student(request):
    SFEO=StudentForms()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForms(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    
    return render(request,'student.html',d)