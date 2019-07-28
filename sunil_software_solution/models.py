from django.db import models

from django.db import models

class Student_Enquiry_Data(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile_no = models.BigIntegerField()
    qualification = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

class FeedbackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    date=models.DateField(max_length=50)
    feedback=models.TextField(max_length=50)

class Course_Update(models.Model):
    course_name=models.CharField(max_length=30)
    start_date=models.DateField(max_length=30)
    course_fee=models.IntegerField()
    faculty_name=models.CharField(max_length=30)
    def __str__(self):
        return self.course_name
