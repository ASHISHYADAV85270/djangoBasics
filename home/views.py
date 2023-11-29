# views mai main logic likha jata hai
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, I am the home page</h1>")


def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")