# Django Static Pages with no Templates

 Created 4 web pages with no style, each page should have the following tags:
        
 1. nav with anchor tags for every page, use | as separator
 2. h1
 3. h2
 4. p
   

Enclosed is the repo with markdown file with blocks of code for: 
* views.py
* urls.py
* settings.py (INSTALLED_APPS only)

Included screenshots for every page.

Use only django.http.HttpResponse, for every page add any of these data (include name and values for every element using f strings with ol or ul tags):

* 3 variables with different data types
* a list of mixed data types of length 6
* a dictionary with string keys and different data types values of length 5


### code

config/settings.py
```Python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'static_pages_1',
]

```

config/urls.py
```Python
from django.contrib import admin
from django.urls import path
from static_pages_1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.Contact, name="contact"),   
    path('about/', views.About, name="about"),
    path('programs/', views.Programs, name="programs"),
]
```

static_pages_no_templates/views.py
```Python
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
        <li>Name: { name }</li>
        <li>Faculty: {faculty}</li>
        <li>Number of Students: {number_of_students}</li>
    </ol>

"""

def home(request):
    content=f"""
    <h1>Welcome to {name}</h1>
    <h2>Empowering Students for a Brighter Future</h2>
    <p>Explore more about our institution</p>
    """

    return HttpResponse(nav + content + home_body)

def Contact(request):
    content = f"""
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
    content = f"""
    <h1>Our Programs</h1>
    <h2>Explore Our Diverse Range of Programs</h2>
    <p>Our programs are designed to provide students with a comprehensive education and prepare them for successful careers in their chosen fields.</p>
    """
    return HttpResponse(nav + content)

```

### Rendering

# Home

<img width="809" height="377" alt="image" src="https://github.com/user-attachments/assets/975d9eb3-5ce8-4310-ab69-39e3ee49f50b" />

# Contact

<img width="502" height="340" alt="image" src="https://github.com/user-attachments/assets/b5e0d860-e5e4-4b83-9316-96f531ffa684" />

# About

<img width="808" height="309" alt="image" src="https://github.com/user-attachments/assets/e850044a-306c-4677-b028-42e5f41d8de4" />

# Programs

<img width="810" height="318" alt="image" src="https://github.com/user-attachments/assets/32a519bc-6fae-4a26-b32d-eef283d8bade" />



