from django.contrib import admin
from kitab.models import *
# Register your models here.

admin.site.register(book)
admin.site.register(subject)
admin.site.register(course)
admin.site.register(stream) 
admin.site.register(course_subject)
admin.site.register(subject_book)
admin.site.register(bookrequest)

