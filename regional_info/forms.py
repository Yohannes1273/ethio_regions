from django import forms
from .models import RegionalInfo

class RegionalInfoForm(forms.ModelForm):
    class Meta:
        model=RegionalInfo
        fields="__all__"