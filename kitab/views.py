from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from kitab.models import *
import json
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
'''
def show_project(request):
	branch_list = branch.objects.all()
	subbranch_list = subbranch.objects.all()
	context = {'branch_list':branch_list , 'subbranch_list':subbranch_list }
	return render(request, 'mutech/show_project.html/1/', context)
'''
def show_book(request, sub_name):
	current_subject = subject.objects.get(subject_name=sub_name)
	book_list = subject_book.objects.all().filter(subject_id_id=current_subject)
	
	'''
	book_dict = {}
	for b in book_list:
		book_dict[b.book_name] = b.book_name
	'''
	
	context = { 'book_list':book_list }
	return render(request, 'kitab/catagaries.html', context)

def howitworks(request):
	stream_list = stream.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	course_list = course.objects.all()
	context = {'subject_list':subject_list ,'book_list':book_list ,'course_list':course_list ,'stream_list':stream_list}
	return render(request, 'kitab/howitworks.html',context)

def get_course(request, strm_id):
    current_stream = stream.objects.get(stream_name=strm_id)
    courses = course.objects.all().filter(stream_id_id=current_stream)

    course_dict = {}
    for c in courses:
        course_dict[c.course_name] = c.course_name

    #data = [course_dict]
    return HttpResponse(json.dumps(course_dict))


def get_subject(request, cours_id):
	current_course = course.objects.get(course_name=cours_id)
	subjects = subject.objects.all().filter(course_id_id=current_course)	
	
	subject_dict = {}
	for s in subjects:
		subject_dict[s.subject_name] = s.subject_name
	
	#data = [subject_dict]	
	return HttpResponse(json.dumps(subject_dict))

'''
def detail(request, stream_id1, course_id2=0, subject_id3=0):

	stream_list = stream.objects.all()
	course_list = course.objects.all()
	subject_list = subject.objects.all()
	book_list = book.objects.all()
	if stream_id1:
		streamId = get_object_or_404(stream, pk=stream_id1)
	context1 = {'course_list':course_list , 'subject_list':subject_list ,'stream_list':stream_list , 'streamId':streamId}

	return render(request, 'kitab/catagaries.html', context1)	
	'''