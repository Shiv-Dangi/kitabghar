from django.db import models
from django.core.validators import RegexValidator
import warnings
warnings.filterwarnings("ignore", "Field 'subbranch_title' doesn't have a default value")
# Create your models here.

class stream(models.Model):
	stream_name = models.CharField(max_length=50)
	stream_desc = models.TextField(max_length=2000)

	def __unicode__(self):              # __str__ on Python 3
        	return str(self.stream_name)

class course(models.Model):
	course_name = models.CharField(max_length=50)
	course_desc = models.TextField(max_length=2000)
	stream_id = models.ForeignKey(stream)

	def __unicode__(self):              
        	return str(self.course_name)        	
        	
class subject(models.Model):
    subject_name = models.CharField(max_length=200)
    stream_id = models.ForeignKey(stream, null = True)
    def __unicode__(self):              
        	return str(self.subject_name)		    	

class book(models.Model):
	book_name = models.CharField(max_length=200)
	book_author = models.CharField(max_length=200)
	book_isbn = models.IntegerField(max_length=13)
	book_edition = models.CharField(max_length=50)
	book_pdf_link = models.CharField(max_length=250)

	def __unicode__(self):              
        	return str(self.book_name)

class course_subject(models.Model):
	course_id = models.ForeignKey(course, null = True)
	subject_id = models.ForeignKey(subject)

	def __unicode__(self):              
        	return str(self.course_id)

class subject_book(models.Model):
	subject_id = models.ForeignKey(subject)
	book_id = models.ForeignKey(book)

	def __unicode__(self):              
        	return str(self.subject_id)

class bookrequest(models.Model):
	user_name = models.CharField(max_length=200)
	user_emailid = models.EmailField(max_length=254)
	book_name = models.CharField(max_length=200)
	book_author = models.CharField(max_length=200)
	book_edition = models.CharField(max_length=50)

	def __unicode__(self):
		return str(self.user_name)

class contactus(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	phone_no = models.BigIntegerField(max_length=13)
	message = models.TextField(max_length=5000)

	def __unicode__(self):              
        	return str(self.fname) 		
		