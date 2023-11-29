# views mai main logic likha jata hai
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
# The home view renders the index.html template and passes a list of people as the 'peoples' context variable.
def home(request):
    # return HttpResponse("<h1>Hello, I am the home page</h1>")
    peoples=[{'name':"ashish","age":10,},{'name':"Harsh","age":22,},{'name':"palak","age":25,}]
    
    #context is used to send data from this views to html
    return render(request,"index.html",context={'peoples':peoples})


def success_page(request):
    # return HttpResponse("<h1>Hey this is a success page</h1>")
    return render(request,"success/index.html")