import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

User =get_user_model()
# Create your models here.
TYPE =[
    ('rent','RENT'),
    ('sale','SALE'),
]

class PropertyType(models.Model):
    name = models.CharField(max_length=20, choices=TYPE)

    def __str__(self):
        return self.name


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    property_type =models.ForeignKey(PropertyType, on_delete= models.CASCADE)
    image =models.ImageField(upload_to="property", null=True, blank=True)
    title =models.CharField(max_length=20, null=True, blank=True)
    description =models.TextField(null=True, blank=True)
    location =models.TextField(null=True, blank=True)
    bedRooms =models.IntegerField(null=True, blank=True)
    bathRooms =models.IntegerField(null=True, blank=True)
    lift =models.BooleanField()
    carParking =models.BooleanField()
    twoWheelerParking =models.BooleanField()
    security =models.BooleanField()
    cctv =models.BooleanField()
    available_from =models.DateTimeField()
    price =models.DecimalField(max_digits=10, decimal_places=2)
    slug =models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.property_type)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.property_type)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("properties:property_detail", kwargs={'pk':self.pk})

    

class PropertyStatus(models.Model):
    property_type =models.ForeignKey(Property, on_delete= models.CASCADE)
    date =models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.property_type)


class PropertyCost(models.Model):
    # property_name =models.ForeignKey(Property, on_delete=models.CASCADE)
    property_type =models.ForeignKey(Property, on_delete=models.CASCADE)
    value =models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.property_type)



class SiteVists(models.Model):
    date =models.DateTimeField(null=True, blank=True)
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    pickUpLocation =models.TextField(null=True, blank=True)
    property_type =models.ForeignKey(Property, on_delete= models.CASCADE)

    def get_absolute_url(self):
        return reverse("properties:bookings_form", kwargs={'pk':self.pk})



BOOKINGS_STATUS =[
    ('on-going','ON-GOING'),
    ('follow','FOLLOW'),
    
]

class Bookings(models.Model):
    property_type =models.ForeignKey(Property, on_delete=models.CASCADE)
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    site =models.ForeignKey(SiteVists, on_delete= models.CASCADE)
    status =models.CharField(max_length=20, choices= BOOKINGS_STATUS)


class Notes(models.Model):
    bookings =models.ForeignKey(Bookings, on_delete= models.CASCADE)
    date =models.DateTimeField(null=True, blank=True)
    notes =models.TextField(null=True, blank=True)
