
from django.shortcuts import render
 #TO RUN THE HTML IN THE PROJECT
from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<h1>this is my homepage</h1>")

def about(request):
    return render(request, 'transport/about.html')
    
def contact(request):
    return HttpResponse("no contact")
def downloading(request):
    return HttpResponse("downloading here")