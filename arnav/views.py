from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request,'projects.html')

def resume(request):
    return render(request,'resume.html')

def contact(request):
    return render(request,'contact.html')

def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        try:
            # Send email
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                'arnavroy688@gmail.com',  # Sender's email address
                ['arnavr285@gmail.com'],  # List of recipient email addresses
                fail_silently=False,
            )
            return JsonResponse({'message': 'Form submission successful'})
        except Exception as e:
            return JsonResponse({'message': f'Error sending email: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)