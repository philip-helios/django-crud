from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['name']
           cn= fm.cleaned_data['contact']
           reg=User(name=nm,contact=cn)
           reg.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

