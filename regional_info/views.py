from django.shortcuts import render,redirect
from . models import RegionalInfo
from .forms import RegionalInfoForm
from django.contrib import messages 
# Create your views here.

def home(request):
    all_regions= RegionalInfo.objects.all()
    context={'all_regions':all_regions}
    return render(request,'regional_info/home.html',context=context)



def create_region(request):
    if request.method=="POST":
        form=RegionalInfoForm(request.POST,request.FILES)
        context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context={'form':form}
            return render(request,'regional_info/create_region.html',context=context)
    else:
        form = RegionalInfoForm()
        context={'form':form}
        return render(request,'regional_info/create_region.html',context=context)


def detail_region(request,pk):
    region=RegionalInfo.objects.get(id=pk)
    context={'region':region}
    return render(request,'regional_info/detail.html',context=context)





def update(request,pk):
    region=RegionalInfo.objects.get(id=pk)
    form=RegionalInfoForm(instance=region)
    if request.method=="POST":
        form=RegionalInfoForm(request.POST,request.FILES,instance=region)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context={'form':form}
            messages.success(request,'invalid form')
            return render(request,'regional_info/detail.html',context=context)
    else:
       
        context={'form':form}
        return render(request,'regional_info/create_region.html',context=context)

def delete(request,pk):
     region=RegionalInfo.objects.get(id=pk)
     if request.method=="POST":
         region.delete()
         messages.success(request,'Deleted successfully')
         return redirect('home')
     else:
        context={'region':region}
        return render(request,'regional_info/delete.html',context=context)
         
from django.contrib.auth.forms import UserCreationForm
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'regional_info/register.html',context=context)
    else:
        form = UserCreationForm()
        context={'form':form}
        return render(request,'regional_info/register.html',context=context)

      
          
     
     
    