from django.shortcuts import render
from .models import Course
from django.http import HttpResponse
from datetime import date
# Create your views here.
def index(request):
    template="<html>""This is the Fucking first view""</html>"
    return HttpResponse(content=template)

def get_date(request):
    today=date.today()
    template = "<html>""Today's date is {}""</html>".format(today)
    return HttpResponse(content=template)

def popular_course_list(request):
    context = {}
    # If the request method is GET
    if request.method == 'GET':
        # Using the objects model manage to read all course list
        # and sort them by total_enrollment descending
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        # Appen the course list as an entry of context dict
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context)