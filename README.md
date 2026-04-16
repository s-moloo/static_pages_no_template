# Django Static Pages with no Templates

# Static Pages 1

## 📌 Project Overview
This is a simple Django-based web application developed to demonstrate the use of Django views, URL routing, and basic HTML rendering without templates.

## 🚀 Features
- 🏠 Home page displaying college information
- 📞 Contact page with basic contact details
- ℹ️ About page describing the institution
- 📚 Programs page showcasing available programs
- 🔗 Navigation bar for easy page switching
- ⚡ Built using Django views without templates (inline HTML)

📁 Code
📂 config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'static_pages_1',
]

📂 config/urls.py

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.Contact, name="contact"),   
    path('about/', views.About, name="about"),
    path('programs/', views.Programs, name="programs"),
]

📂 static_pages_1/views.py

from django.shortcuts import render
from django.http import HttpResponse

nav = """
<nav>
    <a href='/'>Home</a> |
    <a href='/contact/'>Contact</a> |
    <a href='/about/'>About</a> |
    <a href='/programs/'>Programs</a> |
</nav>
"""

name = "ABC College"
faculty = "Faculty of Science"
number_of_students = 5000

home_body = f"""
<ol>
    <li>Name: {name}</li>
    <li>Faculty: {faculty}</li>
    <li>Number of Students: {number_of_students}</li>
</ol>
"""

def home(request):
    content = f"""
    <h1>Welcome to {name}</h1>
    <h2>Empowering Students for a Brighter Future</h2>
    <p>Explore more about our institution</p>
    """
    return HttpResponse(nav + content + home_body)

def Contact(request):
    content = """
    <h1>Contact Us</h1>
    <p>Email: abccollege123.com</p>
    <p>Phone: (123) 456-7890</p>
    """
    return HttpResponse(nav + content)

def About(request):
    content = f"""
    <h1>About Us</h1>
    <h2>{name} is a renowned educational institution</h2>
    <p>Our mission is to empower students with the knowledge and skills they need to succeed</p>
    """
    return HttpResponse(nav + content)

def Programs(request):
    content = """
    <h1>Our Programs</h1>
    <h2>Explore Our Diverse Range of Programs</h2>
    <p>Our programs are designed to prepare students for successful careers.</p>
    """
    return HttpResponse(nav + content)


# Home

<img width="809" height="377" alt="image" src="https://github.com/user-attachments/assets/975d9eb3-5ce8-4310-ab69-39e3ee49f50b" />

# Contact

<img width="502" height="340" alt="image" src="https://github.com/user-attachments/assets/b5e0d860-e5e4-4b83-9316-96f531ffa684" />

# About

<img width="808" height="309" alt="image" src="https://github.com/user-attachments/assets/e850044a-306c-4677-b028-42e5f41d8de4" />

# Programs

<img width="810" height="318" alt="image" src="https://github.com/user-attachments/assets/32a519bc-6fae-4a26-b32d-eef283d8bade" />



