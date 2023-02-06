from django.shortcuts import render,HttpResponseRedirect
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
           fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

# This Function will delete user
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')