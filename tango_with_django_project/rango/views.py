from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm

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

def add_category (request):
	form = CategoryForm()

	if request.method == 'POST':
		form=CategoryForm(request.POST)

		if form.is_valid():
			cat=form.save(commit=True)
			print(cat,cat.slug)
			return index(request)
		else:
			print(form.errors)
	return render (request,'rango/add_category.html',
		{'form':form})



def add_page (request,category_name_slug):
	try:
		category = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category=None
	form=PageForm()
	if request.method=='POST':
		form=PageForm(request.POST)
		if form.is_valid():
			if category:
				page=form.save(commit=False)
				page.category=category
				page.views=0
				page.save()
				return show_category(request,category_name_slug)
		else:
			print(form.errors)
	context_dict={'form':form,'category':category}
	return render(request,'rango/add_page.html',context_dict)
			



