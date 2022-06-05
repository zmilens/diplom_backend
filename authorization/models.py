from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
#create a new user
#create a superuser
class MyAccountManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

def get_profile_image_filepath(self, arg):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "photo/profile_default.png"

class Account(AbstractBaseUser, PermissionsMixin): 
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    name = models.CharField(verbose_name='name', max_length=30, null=True, blank=True) 
    last_name = models.CharField(verbose_name='last_name', max_length=30, null=True, blank=True) 
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    phone = models.CharField(max_length=12, null=True, blank=True) 
    date_of_birth = models.DateField(null=True, blank=True)
    
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD= ['phone']

    def __str__(self):
        return self.email

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin