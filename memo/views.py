from django.shortcuts import render
from django.template import  loader
from django.http import HttpResponse
from memo.models import Schedule

# Create your views here.
def homePage(requset):
    schedule_list = Schedule.objects.all()
    context = {
        'schedule_list': schedule_list,
        'verify_url': "asf",
    }
    return render(requset, 'homePage.html', context)


def input(request):
    return render(request, 'input.html')

def addschedule(request):
    schedule = Schedule()
    schedule.items_title = request.GET['title']
    schedule.items_title = request.GET['content']
    schedule.save()
    return HttpResponse("finish!")

