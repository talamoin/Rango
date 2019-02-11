from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category

def index(request):
	
    context_dict={'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    #return HttpResponse("Rango says hey there partner <a href='/rango/about'> Click here to view the about</a>")
    return render(request,'rango/index.html',context=context_dict)
    
def about(request):
	context_dict={'myvar':"HELLOOO TALA!!\n"}
	return render(request,'rango/about.html',context=context_dict)