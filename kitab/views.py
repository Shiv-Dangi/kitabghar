from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from kitab.models import *
# Create your views here.
def index(request):
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list }
	return render(request, 'kitab/index.html',context)

def header(request):
	return render(request, 'kitab/header.html')

def footer(request):
	return render(request, 'kitab/footer.html')

def sidebar(request):
	stream_list = stream.objects.all()
	course_list = course.objects.all()
	subject_list = subject.objects.all()
	context = {'stream_list':stream_list, 'course_list':course_list, 'subject_list':subject_list }
	return render(request, 'kitab/sidebar.html', context)
'''
def contact(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}
	return render(request, 'kitab/contact.html',context)
'''
def contact(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}

	if request.method == 'GET':
		return render(request, 'kitab/contact.html',context)
	else:
		
		data = contactus(fname= request.POST['fname'], lname= request.POST['lname'], email = request.POST['email'], phone_no = request.POST['phone_no'], message = request.POST['message'])
		data.save()
		return HttpResponseRedirect('#')

def requestbook(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}

	if request.method == 'GET':
		return render(request, 'kitab/requestbook.html',context)
	else:
		''' -----fetching the data from the user and saving it in database---- '''
		data = bookrequest(user_name= request.POST['name'], user_emailid = request.POST['email'], book_name= request.POST['bname'], book_author= request.POST['authorname'], book_edition= request.POST['edn'])
		data.save()
		return HttpResponseRedirect('#')


def aboutus(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}
	return render(request, 'kitab/aboutus.html',context)

def catagaries(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}
	return render(request, 'kitab/catagaries.html',context)

def howitworks(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}
	return render(request, 'kitab/howitworks.html',context)
'''
def requestbook(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}
	return render(request, 'kitab/requestbook.html',context)
'''	