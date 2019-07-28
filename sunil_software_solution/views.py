from django.shortcuts import render
from .forms import *
from .models import *
from django.http.response import HttpResponse
import datetime
date=datetime.datetime.now()
def base_home(request):
    return render(request,'base_home.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == "POST":
        eform =Enquiry_Form(request.POST)
        if eform.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email', '')
            mobile_no = request.POST.get('mobile_no', '')
            qualification = request.POST.get('qualification', '')
            location = request.POST.get('location', '')
            course = request.POST.get('course', '')
            data = Student_Enquiry_Data(
                first_name=first_name,
                last_name=last_name,
                email=email,
                mobile_no=mobile_no,
                qualification=qualification,
                location=location,
                course=course,

            )
            data.save()
            eform =Enquiry_Form()
            return render(request, 'contact.html', {'abc': eform})
        else:

            return HttpResponse('Invalid form')
    else:
        eform =Enquiry_Form()
        return render(request, 'contact.html', {'abc': eform})

def feedback(request):
    if request.method == 'POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name', '')
            rating = request.POST.get('rating', '')
            feedback = request.POST.get('feedback', '')
            data = FeedbackData(
                name=name,

                rating=rating,
                date=date,
                feedback=feedback,
            )
            data.save()
            feedbacks = FeedbackData.objects.all()
            fform = FeedbackForm()
            return render(request, 'feedback.html', {'asdf': fform, 'jkl': feedbacks})
        else:
            return HttpResponse('invalid form')
    else:
        feedbacks = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request, 'feedback.html', {'asdf': fform, 'jkl': feedbacks})

def career(request):
    return render(request,'career.html')
def gallery(request):
    return render(request,'gallery.html')
def login(request):
    return render(request,'login.html')


def Services(request):
    Course_Update_Data=Course_Update.objects.all()
    return render(request,'services.html',{'Course_Update_Data':Course_Update_Data})