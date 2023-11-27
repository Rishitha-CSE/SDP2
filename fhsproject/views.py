from django.shortcuts import render, redirect

def homepage(request):
    return render(request,"home.html")

def indexfunction(request):
    return render(request,"index.html")

def registration(request):
    return render(request,"registration.html")

def login(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"index.html")

def contactfunction(request):
    return render(request,"index.html")

def menufunction(request):
    return render(request,"menu.html")