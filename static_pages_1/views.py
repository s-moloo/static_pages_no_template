from django.shortcuts import render
from django.http import HttpResponse

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

home_body = f"""
    <ol>
        <li>Name: { name}</li>
        <li>Faculty: {faculty}</li>
        <li>Number of Students: {number_of_students}</li>
    </ol>

"""

def home(request):
    content="""
    <h1>Welcome to {name}</h1>
    <h2>Empowering Students for a Brighter Future</h2>
    <p>Explore more about our institution</p>
    """

    return HttpResponse(nav + content + home_body)

def Contact(request):
    content = f"""
    <h1>Contact Us</h1>
    <p>Email: { name }.com</p>
    <p>Phone: (123) 456-7890</p>
    """
    return HttpResponse(nav + content) 


def About(request):
    content = """
    <h1>About Us</h1>
    <h2>{name} is a renowned educational institution</h2>
    <p>Our mission is to empower students with the knowledge and skills they need to succeed</p>
    """
    return HttpResponse(nav + content) 


def Programs(request):
    content = """
    <h1>Our Programs</h1>
    <h2>Explore Our Diverse Range of Programs</h2>
    <p>Our programs are designed to provide students with a comprehensive education and prepare them for successful careers in their chosen fields.</p>
    """
    return HttpResponse(nav + content)