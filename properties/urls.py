from django.urls import path
from .views import PropertyView, PropertyFormView, PropertyDetailView, BookingsFormView, LoginView, RegisterView
from django.contrib.auth.decorators import login_required
app_name= 'properties'

urlpatterns =[
    path('properties/', PropertyView.as_view(), name='property'),
    path('property_form/', PropertyFormView.as_view(), name='property_form'),
    path('property_detail/<uuid:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('bookings_form/', BookingsFormView.as_view(), name='bookings_form'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]