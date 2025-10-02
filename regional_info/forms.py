from django import forms
from .models import RegionalInfo

class RegionalInfoForm(forms.ModelForm):
    region_number = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Region Number'
        })
    )

    name = forms.CharField(
        max_length=64,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Region Name'
        })
    )

    population_size = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Population Size'
        })
    )

    area_in_square = forms.FloatField(
        label="",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Area in Square Kilometers'
        })
    )

    capital_city = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Capital City'
        })
    )

    flag = forms.ImageField(
        label="Flag Image"
    )

    email_address = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )

    map = forms.ImageField(
        label="Map Image"
    )

    website = forms.URLField(
        label="",
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Website URL'
        })
    )
    



    # region_number=models.PositiveSmallIntegerField()
    # name=models.CharField(max_length=64)
    # population_size=models.PositiveBigIntegerField()
    # area_in_square=models.FloatField()
    # capital_city=models.CharField(max_length=100)
    # flag=models.ImageField( upload_to='flag' )
    # email_address=models.EmailField()
    # map=models.ImageField(upload_to='map')
    # website=models.URLField()

    class Meta:
        model=RegionalInfo
        fields="__all__"