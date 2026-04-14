from django.shortcuts import render
from django.http import HttpResponse
nav = """
<nav>
    <a href='/'>Home</a> |
    <a href='/about/'>About</a> |
    <a href='/contact/'>Contact</a> |
    <a href='/services/'>Services</a> |
</nav>
"""

def home(request):
    store_name = "ABC Dentistry Clinic"
    
    store_info = f"<h1>Welcome to {store_name}</h1><h2>Our Services</h2><p>We offer a wide range of dental services, including general dentistry, cosmetic dentistry, orthodontics, and more.Our team of experienced dentists is dedicated to providing high-quality care in a comfortable and friendly environment.</p>"
    content = f"{store_info}"

    return HttpResponse(nav + content)


def About(request): 
    content = f"""
    <h1>About Us</h1>
    <h2>Our Journey</h2>
    <p>Founded in 2010, ABC Dentistry Clinic has been committed to providing exceptional dental care to our community. Our team of skilled dentists and staff work together to create a welcoming and comfortable environment for our patients.</p>
    <h2>Our Mission</h2> """
    return HttpResponse(nav + content)


def Services(request):
    content = f"""
    <h1>Our Services</h1>
    <ul>
        <li><strong>General Dentistry:</strong> Routine check-ups, cleanings, fillings, and preventive care to maintain your oral health.</li>
        <li><strong>Cosmetic Dentistry:</strong> Teeth whitening, veneers, and smile makeovers to enhance the appearance of your smile.</li>
        <li><strong>Orthodontics:</strong> Braces and Invisalign to straighten teeth and correct bite issues.</li>
        <li><strong>Restorative Dentistry:</strong> Crowns, bridges, and dental implants to restore damaged or missing teeth.</li>
    </ul>
    <p>Our team is dedicated to providing personalized care and ensuring that each patient receives the best treatment for their unique needs.</p>  
    """
    return HttpResponse(nav + content)

def Contact(request):
    content = f"""
    <h1>Contact Us</h1>
    <p>If you have any questions or would like to schedule an appointment, please feel free to contact us:</p>
    <ul>
        <li><strong>Address:</strong> 123 Dental Avenue, Smile City</li>
        <li><strong>Phone:</strong> (123) 456-7890</li>
        <li><strong>Email:</strong> info@abcdn.com</li>
    </ul>
    <p>We look forward to hearing from you and helping you achieve a healthy, beautiful smile!</p>
    """
    return HttpResponse(nav + content)



