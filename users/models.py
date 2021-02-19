from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name='user', last_name='new', password=None, is_staff=False, is_admin=False, is_active=False):
        if not email:
            raise ValueError('Email Required')
    
       
        user_obj =self.model(
           email =self.normalize_email(email)
       )
        user_obj.set_password(password)
        user_obj.first_name= first_name
        user_obj.last_name= last_name
        user_obj.is_staff= is_staff
        user_obj.is_admin= is_admin
        user_obj.is_active= is_active
        user_obj.save(using= self._db)
        return user_obj

    def create_Staffuser(self, email, password=None, first_name='new', last_name='user'):
        user =self.create_user(
            email,
            first_name =first_name,
            last_name =last_name,
            password =password,
            is_active =True,
            is_staff =True

        )
        return user

    def create_superuser(self, email, password=None, first_name='new', last_name='user'):
        user =self.create_user(
            email,
            first_name =first_name,
            last_name =last_name,
            password =password,
            is_active =True,
            is_staff =True,
            is_admin =True   
        )
        return user





class User(AbstractBaseUser):
    first_name =models.CharField(max_length=20, null=True, blank=True)
    last_name =models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD ='email'

    REQUIRED_FIELDS =['first_name', 'last_name']

    objects =UserManager()

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserType(models.Model):
    name =models.CharField(max_length=20, null=True, blank=True)
    
    



class ClientType(models.Model):
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    userType =models.ForeignKey(UserType, on_delete= models.CASCADE)
