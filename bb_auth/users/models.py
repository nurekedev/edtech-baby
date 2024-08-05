from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from users.managers import bUserManager

class bUser(AbstractBaseUser, PermissionsMixin):
    MALE = 'male'
    FEMALE = 'female'
    NOT_SPECIFIED = 'not_specified'

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOT_SPECIFIED, 'Not Specified')
    )


    username = None
    email = models.EmailField(_('Email'), max_length=255, unique=True)    
    first_name = models.CharField(_('First name'), max_length=255)
    last_name = models.CharField(_('Last name'), max_length=255)
    gender = models.CharField(_('Gender'), max_length=15, choices=GENDER, default=NOT_SPECIFIED)

    date_joined = models.DateTimeField(_('Date of join'), default=timezone.now)
    date_of_birth = models.DateField(_('Date of birthday'))

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = bUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
          "first_name", 
          "last_name", 
          "date_of_birth",
          "gender",
    ]

    def __str__(self):
            return self.email

class bProfile(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Phone number must be entered in the format: "+7XXXXXXXXXX". Up to 15 digits allowed.')
    phone_number = models.CharField(_('Phone number'), validators=[phone_regex], max_length=17, blank=True)
    avatar = models.ImageField(_('Profile image'), upload_to='profile_photos', blank=True) # default='default-user.jpg')
    

