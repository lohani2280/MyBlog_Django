# A request commes in we send a response.views handles request and returns response  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
	# queryset = Post.objects.all().order_by('-timestamp')
	# the above can be replaced by below by adding a Meta class in modelsPost 		
	queryset_list = Post.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(queryset_list, 5)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		'object_list': queryset , 
		}
	return render(request, 'post_list.html', context)
	

def post_detail(request,id=None):
	instance = get_object_or_404(Post,id=id)
	context = {
		'title' : instance.title,
		'instance': instance
	}
	return render(request, 'post_detail.html', context)	

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=True)
		instance.save()
		messages.success(request, 'Successfully Created')
		return HttpResponseRedirect(instance.get_absolute_url())
	# if request.method == "POST":
	# 	print request.POST
	# 	print request.POST.get('title')
	# 	print request.POST.get('content')
	# The above method is not followed nd thats y we use djago forms

	context = {
		'form':form,
	}
	return render(request, 'post_form.html', context)	


def post_update(request, id=None):	
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=True)
		instance.save()
		messages.success(request, 'Successfully Saved')						
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title' : instance.title,
		'instance': instance,
		'form':form,
	}
	return render(request, 'post_form.html', context)	 			

def post_delete(request, id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request, 'Successfully Deleted')						
	return redirect('list')	 							