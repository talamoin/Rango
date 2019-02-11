from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
	
    #context_dict={'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    #return HttpResponse("Rango says hey there partner <a href='/rango/about'> Click here to view the about</a>")
    
    #return render(request,'rango/index.html',context=context_dict)
    
    category_list=Category.objects.order_by('-likes')[:5]
    

    pages_list=Page.objects.order_by('-views')[:5]
    context_dict={'categories':category_list,"pages":pages_list}
    return render(request,'rango/index.html',context=context_dict)
def about(request):
	context_dict={'myvar':"HELLOOO TALA!!\n"}
	return render(request,'rango/about.html',context=context_dict)

def show_category(request,category_name_slug):
	context_dict={}
	try:
		#see if theres an existing category with the same slug
		category=Category.objects.get(slug=category_name_slug)
		#return all, or an empty list of pages
		pages=Page.objects.filter(category=category)

		context_dict['pages']=pages
		#add the category object
		context_dict['category']=category

	except Category.DoesNotExist:
		#display error message
		context_dict['category']=None
		context_dict['pages']=None

	return render(request,'rango/category.html',context_dict) 