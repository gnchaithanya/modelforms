from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):

    EFTO=TopicForm()
    d={'EFTO':EFTO}

    if request.method=='POST':
        DFTO=TopicForm(request.POST)
        if DFTO.is_valid():
            DFTO.save()
            return HttpResponse('Topic Inserted Successfully!!!!')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EFWO=WebpageForm()
    d={'EFWO':EFWO}
    if request.method=='POST':
        DFWO=WebpageForm(request.POST)
        if DFWO.is_valid():
            DFWO.save()
            return HttpResponse('Webpage Inserted Successfully!!!!')
    return render(request,'insert_webpage.html',d)