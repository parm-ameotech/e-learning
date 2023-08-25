from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(default="default.jpg" ,upload_to='profile_pictures/',blank=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='student')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class Course(models.Model):
    LEVEL_TYPES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    leval = models.CharField(max_length=20, choices=LEVEL_TYPES, default='beginner')
    cover_image = models.ImageField(default="cover_default.jpg" ,upload_to='cover_pictures/',blank=True)
    lectures = models.IntegerField(default='0')
    durations = models.CharField(max_length=10,default='0')
    course_video =models.FileField(upload_to='course_video',null=True,blank=True)
    course_docx = models.FileField(upload_to='course',null=True,blank=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses_taught',null = True)
    price = models.CharField(max_length=10,default='0')


    def __str__(self):
        return self.title