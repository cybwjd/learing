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

//login
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}

<div class="container mt-5" style="max-width:500px;">

    <h2 class="mb-4 text-center">Welcome Back 👋</h2>

    <form>

        <div class="mb-3">
            <label>Email</label>
            <input type="email" class="form-control">
        </div>

        <div class="mb-3">
            <label>Password</label>
            <input type="password" class="form-control">
        </div>

        <button class="btn btn-primary w-100">
            Login
        </button>

    </form>

    <p class="text-center mt-3">
        Don't have an account?
        <a href="{% url 'signup' %}">Sign Up</a>
    </p>

</div>

{% endblock %}


//signup

{% extends 'base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}

<div class="container mt-5" style="max-width:500px;">

    <h2 class="mb-4 text-center">Create Your Account</h2>

    <form>

        <div class="mb-3">
            <label>Full Name</label>
            <input type="text" class="form-control">
        </div>

        <div class="mb-3">
            <label>Email</label>
            <input type="email" class="form-control">
        </div>

        <div class="mb-3">
            <label>Password</label>
            <input type="password" class="form-control">
        </div>

        <button class="btn btn-success w-100">
            Create Account
        </button>

    </form>

    <p class="text-center mt-3">
        Already have an account?
        <a href="{% url 'login' %}">Login</a>
    </p>

</div>

{% endblock %}
