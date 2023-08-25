from django.urls import path,include
from E_learning_app import views

urlpatterns = [
    path("",views.dashboard,name='dashboard'),
    path("profile",views.profile,name='profile'),
    path("course",views.course,name='course'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("logout",views.logout,name='logout'),
    path('add_course',views.add_course,name="add_course")
]
