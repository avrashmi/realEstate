from django.shortcuts import render, get_object_or_404
from .models import Property,PropertyType,PropertyStatus,PropertyCost,SiteVists,Bookings,Notes
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView,CreateView
from .forms import PropertyForm,PropertyForm1,BookingsForm,LoginForm,RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.

class PropertyView(ListView):
    model =Property
    template_name ='properties/properties.html'

    def get_queryset(self, *args, **kwargs):
        # print(self.request.GET.get('q'))
        q =self.request.GET.get('q')
        if q is not None and q != '':
           # qs = super().get_queryset(*args, **kwargs)  
            qs =self.model.objects.filter(location__icontains=q)
            #return qs.filter(location=q) 
            return qs     
        
        
        
        return super().get_queryset(*args, **kwargs)
        


class PropertyFormView(LoginRequiredMixin,FormView):
    
    form_class = PropertyForm1
    template_name ='properties/properties_form.html'
    success_url ='/'



    '''def get_form_kwargs(self, *args, **kwargs):
        kwargs =super().get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return '/' '''

    def form_valid(self, form):
        prop = Property.objects.create(**form.cleaned_data, user=self.request.user)


        return super().form_valid(form)


    
class PropertyDetailView(DetailView):
    model =Property
    template_name ='properties/properties_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["property_status"] = PropertyStatus.objects.filter(property_type= context['object'].id)
        context["property_cost"] = PropertyCost.objects.filter(property_type= context['object'].id)
        return context
    


class BookingsFormView(FormView):
    form_class =BookingsForm
    template_name ='properties/bookings_form.html'
    success_url ='/'

    def form_valid(self, form):
        props =self.request.POST.get('property-type')
        print(props)
        if props is not None:
            prop =get_object_or_404(Property, id=props)

            prop =SiteVists.objects.create(**form.cleaned_data, user=self.request.user, property_type=prop)

        return super().form_valid(form)



    def get_context_data(self, *args, **kwargs):
        context =super().get_context_data(*args, **kwargs)
        context['id'] =self.request.POST.get('property-type')
    
        return context



class LoginView(LoginView):
    form = LoginForm
    template_name = 'properties/login_form.html'


class RegisterView(CreateView):
    form = RegisterForm
    template_name = 'properties/register.html'

    
    


    




























    


