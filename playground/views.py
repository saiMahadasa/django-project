from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    return render(request , 'Hello.html' , {'name' : "sandeep"})

