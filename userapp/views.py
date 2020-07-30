from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegistrationForm,StudentTimetableForm
from django.contrib import messages
from.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'userapp/base.html')


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print("working")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} your account has been created and now you can login!")
            return redirect('/')
    form = UserRegistrationForm()
    context = {
        'form':form,
        }
    return render(request,'userapp/registration.html',context)


@login_required
def addtimetable(request):
    form =  StudentTimetableForm()
    if request.method == 'POST':
        form = StudentTimetableForm(request.POST)
        if form.is_valid():
            monday = form.cleaned_data['monday']
            tuesday = form.cleaned_data['tuesday']
            wednesday = form.cleaned_data['wednesday']
            thursday = form.cleaned_data['thursday']
            friday = form.cleaned_data['friday']
            # profile = form.save(commit = False)
            user = request.user
            p = Profile(user = user,monday = monday,tuesday = tuesday,wednesday=wednesday,thursday=thursday,friday=friday)
            p.save()
            # profile = form.save()
            # profile.user = request.user
            # profile.save()
            return redirect('timetable')
    else:
       form = StudentTimetableForm()
    context = {
        'form':form,
    }
    return render(request,'userapp/add.html',context)



@login_required
def timetable(request):
    timetable = Profile.objects.filter(user=request.user)
    context= {
        'timetable':timetable,
    }
    return render(request,'userapp/timetable.html',context)



def edit(request,pk):
    # item = get_object_or_404(Profile,pk=pk)
    item = Profile.objects.get(id=pk)
    print(item)
    if request.method == 'POST':
        form = StudentTimetableForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('timetable')
    else:
        form = StudentTimetableForm(instance=item)
    return render(request,'userapp/edit.html',{'form':form,})

def delete_timetable(request,pk):
    item = Profile.objects.get(id=pk)
    item.delete()
    return redirect('timetable')






