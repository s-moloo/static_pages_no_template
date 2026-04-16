from os import name

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to ABC College!")

def About(request): 
    return HttpResponse("About Us")

def Contact(request):
    return HttpResponse("Contact Us")

def Programs(request):
    return HttpResponse("Programs")

nav = """
<nav>
    <a href='/'>Home</a> |
    <a href='/about/'>About</a> |
    <a href='/contact/'>Contact</a> |
    <a href='/programs/'>Programs</a> |
</nav>
"""
name = "ABC College"
faculty = "Faculty of Science"
number_of_students = 5000

home_body = f"""<h1>Welcome to {name}!</h1>
<p>We are a prestigious institution dedicated to providing quality education and fostering a vibrant academic community.</p>
<p>Our campus is home to state-of-the-art facilities, a diverse student body, and a wide range of academic programs.</p>
<p>Join us to embark on a journey of knowledge, growth, and success!</p>
"""

def home(request):
    return HttpResponse(nav + home_body)

def About(request):
    about_body = f"""<h1>About Us</h1>
    <p>{name} is a renowned educational institution committed to excellence in teaching, research, and community engagement.</p>
    <p>Our mission is to empower students with the knowledge and skills they need to succeed in their chosen fields and make a positive impact on society.</p>
    <p>With a rich history of academic achievements and a vibrant campus life, {name} offers a supportive and inclusive environment for students to thrive.</p>
    """
    return HttpResponse(nav + about_body) 

def Contact(request):
    contact_body = f"""<h1>Contact Us</h1>
    <p>If you have any questions or would like to learn more about {name}, please feel free to reach out to us.</p>
    <p>Email: contact@{name.lower().replace(' ', '')}.edu</p>
    <p>Phone: (123) 456-7890</p>
    """
    return HttpResponse(nav + contact_body) 

def Programs(request):
    programs_body = f"""<h1>Our Programs</h1>
    <p>{name} offers a wide range of academic programs across various disciplines, including:</p>
    <ul>
        <li>Computer Science</li>
        <li>Business Administration</li>
        <li>Engineering</li>
        <li>Arts and Humanities</li>
        <li>Health Sciences</li>
    </ul>
    <p>Our programs are designed to provide students with a comprehensive education and prepare them for successful careers in their chosen fields.</p>
    """
    return HttpResponse(nav + programs_body)
