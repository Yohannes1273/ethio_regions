from django.shortcuts import render,redirect
from . models import RegionalInfo
from .forms import RegionalInfoForm
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
            return render(request,'regional_info/create_region.html',context=context)
    else:
        form = RegionalInfoForm()
        context={'form':form}
        return render(request,'regional_info/create_region.html',context=context)

    