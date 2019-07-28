from django.contrib import admin
from .models import *
class Admin_Course_Update(admin.ModelAdmin):
    list_display = ['course_name','start_date','course_fee','faculty_name']

admin.site.register(Course_Update,Admin_Course_Update)
admin.site.site_header="SUNIL SOFTWARE SOLUTION"
admin.site.register(FeedbackData)
admin.site.register(Student_Enquiry_Data)

