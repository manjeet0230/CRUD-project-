from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import studentregistration
from .models import User

def  add_show(request):
    # stud=User.objects.all()
    if request.method == "POST":
        fm=studentregistration(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pw=fm.cleaned_data['password']
           reg=User(name=nm,email=em,password=pw)
           reg.save()
           fm=studentregistration()
    else:
         fm=studentregistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})
# Create your views here.

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm= studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=studentregistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})