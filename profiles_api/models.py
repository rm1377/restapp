from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        """Create a new userprofile for the given details"""
        if not email:
            raise ValueError('users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.setpassword(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        """Create a new superuser for the given details"""
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=70, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrive the full name of the user"""
        return self.name

    def get_short_name(self):
        """retrive the short name of the user"""
        return self.name

    def __str__(self):
        return self.email
