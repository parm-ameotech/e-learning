from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as a_login
from django.contrib.auth import logout as a_logout
from .models import Course
from .forms import CourseForm

def dashboard(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def course(request):
    return render(request,'course.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        profile_picture = request.FILES.get('profile_picture')
        mobile_number = request.POST.get('mobile_number')
        user_type = request.POST['user_type']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = CustomUser.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                profile_picture=profile_picture,
                mobile_number=mobile_number,
                user_type=user_type,
                password=password
            )
            messages.success(request, 'User registered successfully.')
            return redirect('login')  # Redirect to the registration page after successful registration
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')  # Redirect back to the registration page with an error message
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            a_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')

def logout(request):
    a_logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')  # Redirect to the home page after logout

def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('course')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})