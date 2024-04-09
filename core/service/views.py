from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def why(request):
    return render(request,'why.html')

def qa(request):
    return render(request,'qa.html')
