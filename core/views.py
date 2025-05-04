from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
  return render(request, 'core/index.html')

def Contact(request):
  if request.method == "POST":
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    msg = request.POST["message"]
    
    newUser = Contact.objects.create(Name=name, Email=email, Subject=subject, Message=msg)
    usermsg = 'Thanks For Contacting Us'
    return render(request, 'core/message.html', {'messg':usermsg})
  return render(request, 'core/contact.html')