from django import forms
from properties.models import Property,SiteVists,User
from django.forms.widgets import NumberInput,PasswordInput,EmailInput

'''class PropertysForm(forms.Form):
    name = forms.CharField(max_length=20)
    location =forms.CharField(widget =forms.Textarea)
    bedRooms =forms.IntegerField()
    bathRooms =forms.IntegerField()
    lift =forms.BooleanField()
    carParking =forms.BooleanField()
    twoWheelerParking =forms.BooleanField()
    security =forms.BooleanField()
    cctv =forms.BooleanField()
    available_from =forms.DateTimeField()
    price =forms.DecimalField(max_digits=5, decimal_places=2)'''


class PropertyForm(forms.ModelForm):
    form_date = forms.DateField(widget= NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Property
        fields = '__all__'
        exclude =['user']

    


    def __init__(self, *args, **kwargs):
        self.user =kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self,commit=True):
        property_name =super().save(commit=False)
        property_name.user = self.user
        if commit:
            property_name.save()
        

class PropertyForm1(forms.ModelForm):
    available_from = forms.DateField(widget= NumberInput(attrs={'type':'date'}))
    class Meta:
         model = Property
         fields ='__all__'
         exclude =['user']







class BookingsForm(forms.ModelForm):
    date =forms.DateField(widget= NumberInput(attrs={'type':'date'}))
    class Meta:
        model =SiteVists
        fields ='__all__'
        exclude =['user', 'property_type']


class LoginForm(forms.Form):
    username =forms.CharField(max_length=20)
    password =forms.CharField(max_length=20, widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    password =forms.CharField(widget= PasswordInput)
    email =forms.CharField(widget= EmailInput)
    class Meta:
        model =User
        fields =['first_name', 'last_name', 'email', 'password']
        
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

    



