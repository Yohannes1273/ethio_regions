from django.shortcuts import render
from . models import RegionalInfo
from .forms import RegionalInfoForm
# Create your views here.

def home(request):
    all_regions= RegionalInfo.objects.all()
    context={'all_regions':all_regions}
    return render(request,'regional_info/home.html',context=context)



def create_region(request):
    form=RegionalInfoForm()
    context={'form':form}
    return render(request,'regional_info/create_region.html',context=context)

    