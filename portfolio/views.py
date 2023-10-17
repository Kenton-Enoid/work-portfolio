from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'portfolio/index.html')

def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        #Send email
        try:
            send_mail(
                subject,
                f'Name: {fullname}\nEmail: {email}\nMobile Number: {mobile_number}\nMessage: {message}', 
                email, ['bonolo.kamolane@gmail.com'],
            )
        except Exception as e:
            print(e)

        return redirect('home')
    
    return render(request, 'portfolio/index.html')