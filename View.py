def login_view(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/signup.html')



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]


//core models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)

    def __str__(self):
        return self.title



core/admin.py

from django.contrib import admin
from .models import Course

admin.site.register(Course)


<a href="{% url 'home' %}">Home</a>
<a href="{% url 'courses' %}">Courses</a>
<a href="{% url 'login' %}">Login</a>
<a href="{% url 'signup' %}">Sign Up</a>
