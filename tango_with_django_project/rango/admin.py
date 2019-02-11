from django.contrib import admin

from rango.models import Category, Page
# Register your models here.



class PageAdmin(admin.ModelAdmin):
	#note, this is not a method !!!
	list_display=("title","category","url")



admin.site.register(Category)
admin.site.register(Page,PageAdmin)