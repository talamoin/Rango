from django.conf.urls import url
from rango import views

#this is all under /rango/
urlpatterns=[
	url(r'^about/',views.about, name='about'),
	url(r'^add_category/$',views.add_category,name='add_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/',views.add_page,name='add_page'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
	url(r'^$',views.index,name='index'),

]