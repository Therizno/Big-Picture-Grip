from django.shortcuts import render

#Website views

def home(request):
    return render(request, "home.html")

def threeTon(request):
    return render(request, "3ton.html")

def fiveTon(request):
    return render(request, "5ton.html")

def giraffe(request):
    return render(request, "giraffe.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
